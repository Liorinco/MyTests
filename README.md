# MyTests

## Sequence diagram

![Alt text](https://g.gravizo.com/source/svg/custom_mark10?https%3A%2F%2Fgithub.com%2FLiorinco%2FMyTests%2Fblob%2Fmaster%2FREADME.md)
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

<img src='https://g.gravizo.com/source/svg?digraph%20G%20%7Bmain%20-%3E%20parse%20-%3E%20execute%3B%20main%20-%3E%20init%3B%20main%20-%3E%20cleanup%3B%20execute%20-%3E%20make_string%3B%20execute%20-%3E%20printf%3B%20init%20-%3E%20make_string%3B%20main%20-%3E%20printf%3B%20execute%20-%3E%20compare%3B%7D'/>
