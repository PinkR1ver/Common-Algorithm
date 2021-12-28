# Decision Trees

https://www.youtube.com/watch?v=7VeUPuFGJHk&t=209s

## How to build Decision Trees by yes/no

1. Calculate all of the Gini impurity scores
    > Gini was developed by the Italian statistician and sociologist Corrado Gini and published in his 1912 paper Variability and Mutability (Italian: Variabilità e mutabilità).

    Because None of the lead nodes are 100% Yes or 100% No, so we can use **Gini** to measure impurity. 
    For example, leaf Gini:
    ![Gini Calculation](Pictures/Screenshot%20from%202021-12-27%2019-40-25.png)
2. If the node itself has the lowest score, than there is no point in separating the patientsany more and it becomes a leaf node
3. If separating the data results in an imporvement, than pick the separation with the lowest impurity value.

## For not yes/no node

### For numeric data
![numeric data gini calculate](Pictures/Screenshot%20from%202021-12-27%2019-58-00.png)
1. Sort the data
2. Calculate the average number for all adjcent patients
3. Calculate the impurity values for each average number

### For ranked data
Calculate Rank <= N, N = 1,2,...,i-1 (Have ith Rank)
> Remember don't calculate Rank <= i, because that would include everyone.

### For multiple choices
Using Permutations
For example, Color Choice: Green, Blue, Red, you can:
* (Color Choice: Blue)
* (Color Choice: Green)
* (Color Choice: Red)
* (Color Choice: Blue or Green)
* (Color Choice: Blue or Red)
* (Color Choice: Red or Green)
> Note: don't calculate impurity score for choose all choice because that would include everyone

# For more information about decision tree, you can find in this website:
https://www.datacamp.com/community/tutorials/decision-tree-classification-python
> Note: This ReadMe.md introduced the decision tree is created by Gini index, called CART(Classification and Regression Tree). There are other algorithm to build different decision trees, using Entropy or something. You can find it in this website.