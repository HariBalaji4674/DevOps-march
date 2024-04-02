## Python DSA Notes

**What is DSA:**
- *Data Structures :*
  - Study of methods for storing and organizing the data in a formal structure is called Data Structuring
  - DS are the essential components that help organize and store data efficiently in computer memory

- *Managing the DS :* `There are 4 types in Managing the data`
  - Insertion
  - Deletion
  - Updation
  - Accessing
- *Types of Data Strucures :*
  - Arrays
  - LinkedList
  - Stacks
  - Queues
  - Trees
  - Graphs
  - Hash
  - Graph
  - String
- **Algorithims:**
  - When we use some sequence of steps to organize and storing the data is called Algorithims
  - set of rules to obtain the expected output from the given input

## Data Structures:

- **Arrays**
    - `Array is a Linear Data Structure stores a collection of elements of the same data type`
    - `Elements are allocated in a contiguous location`
    - `Each Element has unique index`
    - `Allowing for constant time access`
  - **Operations on Arrays**
    - Traversal: Iterating over all elements in an array
    - Insertion: Adding or Updating an element at specific index
    - Deletion: Removing an Element from an array by using an index
    - Searching: Finding an Element in an array by its value or index
  - **Types of Arrays**
    - One Dimensional Array
    - Multi-Dimensional Array
  - **Applications of Arrays**
    - Storing data in a Sequential Manner
    - Implementing queues,stacks and other data structures
    - Representing Matrices and tables
- **Strings**
    - `String is a sequence of characters, Typically used to represent text.`
    - `String is used for manipulating and processing of data in computer programs`
  - **Operations on String**
    - Concatenation: `Joining two strings together.`
    - Comparison: `Comparing two strings lexicographically.`
    - Substring extraction: `Extracting a substring from a string.`
    - Search: `Searching for a substring within a string.`
    - Modification: `Changing or replacing characters within a string.`
  - **Applications of String**
    - Text Processsing
    - Data Validation
    - Data Manipulation
    - Pattern Matching
    - Data Base Management

## What is Time Complexity:


### Asymptotic Analysis
- No dependency in machine,programming language,CPU Cycles etc..
- We Do not have to implement all the ideas/algorithims
- Asymptotic Analysis is measusing the order of growth in the form of input sizes.
- Analysis of algorithms is the determination of the amount of time and space resources required to execute it.

***Reverse String***
```
for i in range(10):
  for j in range(i):
    print(i,end=" ")
```