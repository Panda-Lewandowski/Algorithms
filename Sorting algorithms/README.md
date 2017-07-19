# Sorting algorithms
    In computer science a sorting algorithm is an algorithm that puts elements of a list in a certain order. The most-used
    orders are numerical order and lexicographical order. Efficient sorting is important for optimizing the use of other 
    algorithms (such as search and merge algorithms) which require input data to be in sorted lists; it is also often useful
    for canonicalizing data and for producing human-readable output. [Wiki]
    
## Exchange sorts
### Bubble Sort
![Imgur](http://i.imgur.com/sAvHPFT.gif)
#### Idea
Simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list. Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort. It can be practical if the input is usually in sorted order but may occasionally have some out-of-order elements nearly in position.
#### Advantages
* Simple 
* Can detect that the list is sorted efficiently 
#### Disadvantages
* Slow
#### Possible Improvements
*  The n-th pass finds the n-th largest element and puts it into its final place. So, the inner loop can avoid looking at the last n − 1 items when running for the n-th time.
* More than one element is placed in their final position on a single pass. In particular, after every pass, all elements after the last swap are sorted, and do not need to be checked again.
#### Complexity 
O(n^2) 
#### Stability
* Stable
## Selection sorts
## Insertion sorts
## Merge sorts

## Literature and links
* Knuth, Donald E., Sorting and Searching, The Art of Computer Programming, 3 
*  <a href='https://rosettacode.org/wiki/Category:Sorting_Algorithms'>RosettaCode::Sorting Algorithms</a>
* <a href="http://algolist.manual.ru/">AlgoList</a>
