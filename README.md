# MyTests

## Sequence diagram

![Alt text](https://g.gravizo.com/svg?https%3A%2F%2Fgithub.com%2FLiorinco%2FMyTests%2Fblob%2Fmaster%2FREADME.md)
<details> 
<summary></summary>
custom_mark10
  digraph G {
    aize ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf};
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }
custom_mark10
</details>

![Alt text](http://g.gravizo.com/source?https%3A%2F%2Fbitbucket.org%2FTLmaK0%2Fgravizo-example%2Fraw%2Fmaster%2Fsource.uml)
