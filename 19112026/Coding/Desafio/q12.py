def  calcular_salario():
     sal = float(input("Informe o seu salário (use . para casas decimais): "))
     bonus = sal + (sal / 10)
     print(f"Salário após o bônus aplicado: ${round(bonus, 2)}")
calcular_salario()