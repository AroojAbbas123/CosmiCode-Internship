import os
import csv
import json
import asyncio
import threading
import random
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timedelta

@dataclass
class DataRecord:
    """Class to represent a single data record"""
    id: int
    values: Dict[str, float]
    category: str = "default"
    metadata: Dict[str, Any] = field(default_factory=dict)

class EnhancedFileHandler:
    """Extended file handler with support for multiple formats"""
    def __init__(self, filename: str):
        self.filename = filename
        self.lock = threading.Lock()
    
    async def read_async(self) -> str:
        """Asynchronously read file content"""
        try:
            async with asyncio.Lock():
                with open(self.filename, 'r') as file:
                    await asyncio.sleep(0.1)
                    return file.read()
        except (FileNotFoundError, IOError) as e:
            return f"Error: {str(e)}"
    
    def read(self) -> str:
        """Read entire file content"""
        with self.lock:
            try:
                with open(self.filename, 'r') as file:
                    return file.read()
            except FileNotFoundError:
                return "File not found"
            except IOError as e:
                return f"Error reading file: {str(e)}"
    
    def write(self, content: str) -> bool:
        """Overwrite file with new content"""
        with self.lock:
            try:
                with open(self.filename, 'w') as file:
                    file.write(content)
                return True
            except IOError:
                return False
    
    def append(self, content: str) -> bool:
        """Add content to end of file"""
        with self.lock:
            try:
                with open(self.filename, 'a') as file:
                    file.write(content)
                return True
            except IOError:
                return False
    
    def clear(self) -> bool:
        """Empty the file"""
        return self.write("")
    
    def read_lines(self) -> List[str]:
        """Read file as list of lines"""
        with self.lock:
            try:
                with open(self.filename, 'r') as file:
                    return [line.strip() for line in file.readlines()]
            except FileNotFoundError:
                return []
    
    def export_csv(self, data: List[Dict], headers: Optional[List[str]] = None) -> bool:
        """Export data to CSV file"""
        if not data:
            return False
            
        if headers is None:
            headers = list(data[0].keys())
        
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
            return True
        except IOError:
            return False
    
    def export_json(self, data: Any) -> bool:
        """Export data to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=2)
            return True
        except IOError:
            return False
    
    def __str__(self):
        return f"EnhancedFileHandler for '{self.filename}'"

class DataAnalyzer:
    """Core data analysis functionality"""
    def __init__(self):
        self.data: List[DataRecord] = []
        self.stats_cache = {}
        self.executor = ThreadPoolExecutor(max_workers=4)
    
    async def load_data_async(self, filepath: str) -> bool:
        """Asynchronously load data from file"""
        handler = EnhancedFileHandler(filepath)
        content = await handler.read_async()
        
        if content.startswith("Error"):
            return False
        
        try:
            if filepath.endswith('.json'):
                json_data = json.loads(content)
                self.data = [DataRecord(**item) for item in json_data]
            elif filepath.endswith('.csv'):
                self.data = []
                reader = csv.DictReader(content.splitlines())
                for row in reader:
                    try:
                        values = {k: float(v) for k, v in row.items() if k not in ['id', 'category']}
                        record = DataRecord(
                            id=int(row.get('id', 0)),
                            values=values,
                            category=row.get('category', 'default')
                        )
                        self.data.append(record)
                    except (ValueError, KeyError):
                        continue
            return True
        except (json.JSONDecodeError, csv.Error):
            return False
    
    def load_data(self, filepath: str) -> bool:
        """Load data from file"""
        handler = EnhancedFileHandler(filepath)
        content = handler.read()
        
        if content.startswith("Error"):
            return False
        
        try:
            if filepath.endswith('.json'):
                json_data = json.loads(content)
                self.data = [DataRecord(**item) for item in json_data]
            elif filepath.endswith('.csv'):
                self.data = []
                reader = csv.DictReader(content.splitlines())
                for row in reader:
                    try:
                        values = {k: float(v) for k, v in row.items() if k not in ['id', 'category']}
                        record = DataRecord(
                            id=int(row.get('id', 0)),
                            values=values,
                            category=row.get('category', 'default')
                        )
                        self.data.append(record)
                    except (ValueError, KeyError):
                        continue
            return True
        except (json.JSONDecodeError, csv.Error):
            return False
    
    def calculate_stats(self) -> Dict[str, Dict[str, float]]:
        """Calculate statistics for all numeric fields"""
        if not self.data:
            return {}
        
        def _calculate_for_field(field: str) -> tuple:
            values = [record.values.get(field, 0) for record in self.data]
            return (
                field,
                {
                    'mean': sum(values) / len(values),
                    'min': min(values),
                    'max': max(values),
                    'count': len(values)
                }
            )
        
        fields = set()
        for record in self.data:
            fields.update(record.values.keys())
        
        results = {}
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(_calculate_for_field, field) for field in fields]
            for future in futures:
                field, stats = future.result()
                results[field] = stats
        
        self.stats_cache = results
        return results
    
    def filter_data(self, condition: callable) -> List[DataRecord]:
        """Filter data based on a condition function"""
        return [record for record in self.data if condition(record)]
    
    def show_text_visualization(self, field: str):
        """Simple text-based visualization"""
        if not self.data:
            print("No data to visualize")
            return
        
        values = [record.values.get(field, 0) for record in self.data]
        min_val = min(values)
        max_val = max(values)
        avg_val = sum(values) / len(values)
        
        print(f"\nText Visualization for {field}:")
        print(f"Minimum: {min_val:.2f}")
        print(f"Maximum: {max_val:.2f}")
        print(f"Average: {avg_val:.2f}")
        print("\nDistribution:")
        
        # Simple histogram using text
        hist, bins = self._create_text_histogram(values)
        for i in range(len(hist)):
            print(f"{bins[i]:.1f}-{bins[i+1]:.1f}: {'*' * hist[i]}")
    
    def _create_text_histogram(self, values, bins=10):
        """Helper function to create text histogram"""
        min_val = min(values)
        max_val = max(values)
        bin_width = (max_val - min_val) / bins
        
        hist = [0] * bins
        for value in values:
            bin_idx = min(int((value - min_val) / bin_width), bins - 1)
            hist[bin_idx] += 1
        
        bin_edges = [min_val + i * bin_width for i in range(bins + 1)]
        return hist, bin_edges
    
    def export_results(self, filepath: str, format: str = 'csv') -> bool:
        """Export analysis results"""
        handler = EnhancedFileHandler(filepath)
        
        if format == 'csv':
            export_data = []
            for record in self.data:
                row = {'id': record.id, 'category': record.category}
                row.update(record.values)
                export_data.append(row)
            return handler.export_csv(export_data)
        elif format == 'json':
            export_data = [{'id': record.id, 'category': record.category, **record.values} 
                          for record in self.data]
            return handler.export_json(export_data)
        else:
            return False

class DataAnalysisApp:
    """Main application class"""
    def __init__(self):
        self.analyzer = DataAnalyzer()
        self.running = False
    
    async def run_async(self):
        """Run the application with async capabilities"""
        self.running = True
        print("Data Analysis Application (Text-Only Version)")
        print("--------------------------------------------")
        
        while self.running:
            print("\nMenu:")
            print("1. Load data")
            print("2. View statistics")
            print("3. Filter data")
            print("4. Show text visualization")
            print("5. Export results")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                filepath = input("Enter file path: ")
                if await self.analyzer.load_data_async(filepath):
                    print("Data loaded successfully!")
                else:
                    print("Failed to load data")
            
            elif choice == '2':
                stats = self.analyzer.calculate_stats()
                if stats:
                    print("\nStatistics:")
                    for field, values in stats.items():
                        print(f"\n{field}:")
                        for stat, value in values.items():
                            print(f"  {stat}: {value:.2f}")
                else:
                    print("No data to analyze")
            
            elif choice == '3':
                if not self.analyzer.data:
                    print("No data loaded")
                    continue
                
                field = input("Enter field to filter on: ")
                op = input("Enter operator (>, <, ==, >=, <=): ")
                value = float(input("Enter value: "))
                
                def condition(record):
                    try:
                        field_value = record.values.get(field, 0)
                        if op == '>': return field_value > value
                        if op == '<': return field_value < value
                        if op == '==': return field_value == value
                        if op == '>=': return field_value >= value
                        if op == '<=': return field_value <= value
                        return False
                    except (ValueError, TypeError):
                        return False
                
                filtered = self.analyzer.filter_data(condition)
                print(f"\nFound {len(filtered)} matching records:")
                for record in filtered[:5]:
                    print(f"ID: {record.id}, {field}: {record.values.get(field, 'N/A')}")
            
            elif choice == '4':
                if not self.analyzer.data:
                    print("No data loaded")
                    continue
                
                field = input("Enter field to visualize: ")
                self.analyzer.show_text_visualization(field)
            
            elif choice == '5':
                if not self.analyzer.data:
                    print("No data loaded")
                    continue
                
                filepath = input("Enter output file path: ")
                format = input("Enter format (csv/json): ")
                if self.analyzer.export_results(filepath, format):
                    print("Export successful!")
                else:
                    print("Export failed")
            
            elif choice == '6':
                self.running = False
                print("Exiting application...")
            
            else:
                print("Invalid choice, please try again")

def generate_sample_data(filepath: str, format: str = 'json', num_records: int = 50):
    """Generate sample data without external dependencies"""
    cities = ["New York", "London", "Tokyo", "Paris", "Berlin", "Sydney"]
    categories = ["A", "B", "C", "D"]
    
    data = []
    for i in range(num_records):
        # Generate random timestamp within the last year
        timestamp = (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat()
        
        record = {
            'id': i + 1,
            'category': random.choice(categories),
            'values': {
                'temperature': round(random.uniform(10, 30), 2),
                'humidity': round(random.uniform(30, 90), 2),
                'pressure': round(random.uniform(900, 1100), 2),
                'speed': round(random.uniform(0, 100), 2)
            },
            'metadata': {
                'location': random.choice(cities),
                'timestamp': timestamp
            }
        }
        data.append(record)
    
    handler = EnhancedFileHandler(filepath)
    if format == 'json':
        handler.export_json(data)
    else:
        csv_data = []
        for record in data:
            row = {'id': record['id'], 'category': record['category']}
            row.update(record['values'])
            csv_data.append(row)
        handler.export_csv(csv_data)

async def main():
    # Create sample data if needed
    sample_json = "sample_data.json"
    sample_csv = "sample_data.csv"
    
    if not os.path.exists(sample_json):
        generate_sample_data(sample_json)
        print(f"Created sample data file: {sample_json}")
    if not os.path.exists(sample_csv):
        generate_sample_data(sample_csv, format='csv')
        print(f"Created sample data file: {sample_csv}")
    
    # Run the application
    app = DataAnalysisApp()
    await app.run_async()

if __name__ == "__main__":
    asyncio.run(main())