# Discussion.md

## Solutions Considered

1. **Reading the Entire File at Once (Inefficient)**
   - Initially, I considered reading the entire log file into memory and filtering logs based on the given date.
   - **Issue:** Since the file is **~1TB**, loading it entirely would cause memory overflow and extreme inefficiency.

2. **Line-by-Line Processing (Efficient)**
   - Instead of loading the entire file, I opted to process the log file **line by line**.
   - This approach ensures that memory usage remains minimal.
   - **Advantage:** Works efficiently even for large files as it doesn't load unnecessary data.

3. **Using Grep (Not Cross-Platform)**
   - Using system commands like `grep "YYYY-MM-DD"` could be an option, but it is not cross-platform (not available on Windows natively).
   - **Rejected** because the solution should work on all operating systems.

## Final Solution Summary

The final implementation reads the log file **line by line**, extracts entries matching the input date, and writes them to an output file.  

### **Why This Approach?**
✅ **Memory Efficient:** Processes one line at a time instead of loading the whole file.  
✅ **Scalability:** Works even for very large files (~1TB).  
✅ **Cross-Platform:** Works on **Windows, Linux, and macOS** without dependencies.  

## Steps to Run

1. **Ensure Python is Installed**
   - Run `python --version` to check if Python is installed.

2. **Navigate to the Project Folder**
   ```sh
   cd tech-campus-recruitment-2025/src
