Program Conversor ;

Var
	med:integer;
	value,c,f:real;

Begin
	writeln ('Olá, informe a medida para a conversão!(C = 1/ F = 2)');
	readln (med);
	writeln ('Informe o valor a ser convertido');
	readln (value);
	if med = 1 then
		Begin
	  writeln ('Você está convertendo de C° para F°');
	  f:=((value/5)*9)+32;
		writeln ('O valor em F° é: ', f) ;
		end;
	if med = 2 then
		Begin
	  writeln ('Você está convertendo de F° para C°');
	  c:=((value - 32)/9)*5;
		writeln ('O valor em F° é: ', f) ;
		end;	
	
	
	
End.