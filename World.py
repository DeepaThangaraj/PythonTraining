print("Interest Calculator:")
amount=float(input("Pricipal amount?"))
roi=float(input("Interest rate?"))
years=int(input("Duration in years?"))
total=(amount*pow(1+(roi/100),years))
interest=total-amount
print("\nInterest =%0.2f" %interest)


             
