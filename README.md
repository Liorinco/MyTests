# MyTests

## Sequence diagram

![Alt text](http://g.gravizo.com/source/gravizosample?https://github.com/Liorinco/MyTests/blob/master/README.md#
gravizosample
 digraph G {
   main -> parse -> execute
   main -> init
   main -> cleanup
   execute -> make_string
   execute -> printf
   init -> make_string
   main -> printf
   execute -> compare
 }
gravizosample
)

![Alt text](http://g.gravizo.com/source?https%3A%2F%2Fbitbucket.org%2FTLmaK0%2Fgravizo-example%2Fraw%2Fmaster%2Fsource.uml)
