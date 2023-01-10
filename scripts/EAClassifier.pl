activity(mustEA):-
	mainAct(true), write('reason: 0 mainAct'),nl.
	
activity(mustIA):-
	not(mainAct(true)), ifTrue(true), not(exTrue(true)), sysActNoData(true),
	write('reason: 1 ifTrue and not exTrue and sysActNoData'),nl;
	not(mainAct(true)), noDefault(true), write('reason: 3 noDefault'),nl;
	debug(true),write('reason: 3 debug'),nl.
	
activity(mustEA):-
	
	clsInvoke(true),write('reason: 4 clsInvoke or actInvoke'),nl;
	actInvoke(true),write('reason: 4 clsInvoke or actInvoke'),nl;
	clsDeclare(true),write('reason: 5 clsDeclare'),nl;
	priority(true),write('reason: 6 priority or permission'),nl;
	permission(true),write('reason: 6 priority or permission'),nl.
	
activity(mayIA):-
	similar(true),write('reason: 7 similar'),nl.
	
activity(mayIA):-
	highRatio(true),write('reason: 8 highRatio'),nl.
	
activity(mayEA):-
	exTrue(true),write('reason: 9 exTrue'),nl.
	
activity(mayIA):-
	not(exTrue(true)), ifTrue(true), write('reason: 10 ifTrue and not exTrue '),nl.


top_goal(X) :- activity(X).

solve :-
 top_goal(X),
 write('result: '),write(X), nl.
solve :-
 write('No answer found.'), nl.
