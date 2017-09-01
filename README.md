# MyTests

## Sequence diagram

```sequence
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
```

![Alt text](https://g.gravizo.com/source/svg/custom_mark10?https%3A%2F%2Fgithub.com%2FLiorinco%2FMyTests%2Fblob%2Fmaster%2FREADME.md)
custom_mark10 digraph G { aize ="4,4"; main [shape=box]; main->parse [weight=8]; parse->execute; main->init [style=dotted]; main->cleanup; execute->{make_string; printf}; init->make_string; edge [color=red]; main->printf [style=bold,label="100 times"]; make_string [label="make a string"]; node [shape=box,style=filled,color=".7 .3 1.0"]; execute->compare; } custom_mark10

<img src='https://g.gravizo.com/source/svg?digraph%20G%20%7Bmain%20-%3E%20parse%20-%3E%20execute%3B%20main%20-%3E%20init%3B%20main%20-%3E%20cleanup%3B%20execute%20-%3E%20make_string%3B%20execute%20-%3E%20printf%3B%20init%20-%3E%20make_string%3B%20main%20-%3E%20printf%3B%20execute%20-%3E%20compare%3B%7D'/>

<img src='https://g.gravizo.com/svg?
 digraph G {
   main -> parse -> execute;
   main -> init;
   main -> cleanup;
   execute -> make_string;
   execute -> printf
   init -> make_string;
   main -> printf;
   execute -> compare;
 }
'/>

<img src='https://g.gravizo.com/svg?
@startuml;

actor User;
participant "First Class" as A;
participant "Second Class" as B;
participant "Last Class" as C;

User -> A: DoWork;
activate A;

A -> B: Create Request;
activate B;

B -> C: DoWork;
activate C;

C --> B: WorkDone;
destroy C;

B --> A: Request Created;
deactivate B;

A --> User: Done;
deactivate A;

@enduml
'>

![Alt text](http://yuml.me/diagram/plain/class/%2F%2F Cool Class Diagram, [Customer|-forname:string;surname:string|doShiz()]<>-orders*>[Order], [Order]++-0..*>[LineItem], [Order]-[note:Aggregate root{bg:wheat}])

![Alt text](http://yuml.me/diagram/plain/class/%2F%2F%20Cool%20Class%20Diagram%2C%20%5BCustomer%7C-forname%3Astring%3Bsurname%3Astring%7CdoShiz%28%29%5D%3C%3E-orders%2A%3E%5BOrder%5D%2C%20%5BTrololol%5D%2B%2B-0..%2A%3E%5BLineItem%5D%2C%20%5BOrder%5D-%5Bnote%3AAggregate%20root%7Bbg%3Awheat%7D%5D)

```plantuml svg
@startuml
actor Bob #red
' The only difference between actor
'and participant is the drawing
participant Alice
participant "I have a really\nlong name" as L #99FF99
/' You can also declare:
participant L as "I have a really\nlong name" #99FF99
'/
Alice->Bob: Authentication Request
Bob->Alice: Authentication Response
Bob->L: Log transaction
@enduml
```
