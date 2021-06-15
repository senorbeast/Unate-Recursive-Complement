# urc
Finds complement of Boolean Expression using Unate Recursive paradigm

#What is Unate Recurisve Complement?
The Unate Recursive Paradigm (URP) idea todetermine tautology for a Boolean function represented as a cube list using the Positional CubeNotation (PCN). It turns out that many common Boolean computations can be done using the
URP ideas.

Algorithm Overview:

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

Here cubelist which basically represents a sum of product terms of boolean variables. 
Now you might think what is so difficult about finding a complement of a SOP but now think if we need to find complement of a SOP with 10 variables and 200 SOPs and now we realize this gets difficult and so we need to come up with a algorithm to find out the complement.
