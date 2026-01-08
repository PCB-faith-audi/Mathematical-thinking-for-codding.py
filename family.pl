% Facts: defining parent relationships.

parent(john, mary).
parent(mary, susan).
parent(mary, David).
parent(susan, alice).
 
% Rule: defining ancestor relationships.
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

 % Query examples:

% To find all ancestors of alice, you would ask:

% ?- ancestor(X, alice).