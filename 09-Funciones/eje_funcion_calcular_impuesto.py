#Calcular impuesto  pago_total = pago_sin_impuesto + (pago_sin_puesto*(impuesto/100))

def calculadoraDeImpuesto(pago_sin_impuesto, interes):
    pago_total= pago_sin_impuesto + (pago_sin_impuesto*(interes/100))
    return pago_total

pago=float(input('Proporcione el pago sin impuestos: '))
interes=float(input('Proporcione el interes: ')) 
res=calculadoraDeImpuesto(pago,interes)
print(f'El pago total es: {res}')