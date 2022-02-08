# URC
Finds complement of Boolean Expression using Unate Recursive paradigm

## What is Unate Recursive Complement?
The Unate Recursive Paradigm (URP) idea to determine tautology for a Boolean expression represented as a cube list using the Positional CubeNotation (PCN). It turns out that many common Boolean computations can be done using the
URP ideas.

Where Cubes represent the minterms, and cubelist represents the list of minterms.

### Algorithm Overview:
```
cubeList Complement( cubeList 𝐹 ) {
    // check if 𝐹 is simple enough to complement it directly and quit
    if ( 𝐹 is simple and we can complement it directly )
        return( directly computed complement of 𝐹 )
    else {
        // do recursion
        let 𝑥 = most binate variable for splitting
        cubeList 𝑃 = Complement( positiveCofactor( 𝐹, 𝑥 ) )
        cubeList 𝑁 = Complement( negativeCofactor( 𝐹, 𝑥 ) )
        𝑃 = AND( 𝑥, 𝑃 )
        𝑁 = AND( 𝑥̅, 𝑁 )
        return( OR( 𝑃, 𝑁 ) )
    } // end recursion
} // end function
```

Here cubelist which basically represents a sum of product terms of boolean variables. 
Now you might think what is so difficult about finding a complement of a SOP but now think if we need to find complement of a SOP with 10 variables and 200 SOPs and now we realize this gets difficult and so we need to come up with a algorithm to find out the complement.

### Unate Recursive Paradigm approach works on :
* Finding the most binate variable for splitting  
* Decompose the cubelist with the help of Shannon's Expansion and the most binate variable 
* Recursively decompose the cubelist
* With end condition that the we can directly find the complement of a simple decomposed cubelist.

### Input and Output
  
#### Input file format 
Suppose we have the following Bollean Expression:

    F(x1,x2,x3,x4,x5) = x2x3x4 + x1'x5 + x1x3'x4'
Then the input file format would look like this:

    5                           // Indicates no. of variables               
    3                           // Indicates no. of minterms or cubes
    3 2 3 4                     // Represents individual minterm or cube 
    2 -1 5                      // Represents individual minterm or cube
    3 1 -3 -4                   // Represents individual minterm or cube  
    
    // The first digit of every minterm or cube line represents number of variables in the particular minterm.
    // The following digits of the minterm line represent the whether the variable is in true or complement form
    
    
#### Output file follows the same convention
The Output file contains the complemented Boolean expression, done by Unate Recursive Paradigm

