from django.db import models


class Motorista(models.Model):
    CATEGORIAS_CNH = [
        ('A', 'Categoria A'),
        ('B', 'Categoria B'),
        ('C', 'Categoria C'),
        ('D', 'Categoria D'),
        ('E', 'Categoria E'),
    ]

    TIPOS_SANGUINEOS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    num_cnh = models.CharField(max_length=20)
    tipo_cnh = models.CharField(max_length=1, choices= CATEGORIAS_CNH)
    tipo_sangue = models.CharField(max_length=3, choices=TIPOS_SANGUINEOS)
    email = models.EmailField()
    cel = models.CharField(max_length=20)
    endereco = models.TextField()
    ingresso = models.DateField()
    saiu = models.BooleanField(default=False)
    chegou = models.BooleanField(default=False)

    def __str__(self):
            return self.nome

class Veiculo(models.Model):
    COMBUSTIVEIS = [
        ('G', 'Gasolina'),
        ('A', 'Álcool'),
        ('D', 'Diesel'),
        ('F', 'Flex'),
        ('E', 'Veículo Elétrico')
    ]

    CAMBIOS = [
    ('MANUAL', 'Manual'),
    ('AUTOMATICO', 'Automático'),
    ('AUTOMATIZADO', 'Automatizado'),
    ('CVT', 'CVT'),
    ('DCT', 'Dupla embreagem (DCT)'),
]

    apelido = models.CharField(max_length=300)
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=200)
    ano =models.IntegerField()
    cor = models.CharField(max_length=100)
    tipo_combustivel = models.CharField(max_length = 1, choices = COMBUSTIVEIS)
    tipo_cambio = models.CharField(max_length=12, choices= CAMBIOS)
    quilometragem = models.IntegerField()
    capacidade =models.IntegerField()
    observacao = models.TextField()
    motoristas = models.ManyToManyField(Motorista, related_name='veiculos')
    is_funcionando = models.BooleanField(default =True)
    is_quebrado = models.BooleanField(default =False)
    is_conserto = models.BooleanField(default =False)
    

    def __str__(self):
        return self.apelido

class Rota (models.Model):
    nome = models.CharField(max_length=200)
    motoristas = models.ManyToManyField(Motorista, related_name='rotas')
    duracao = models.DurationField()
    origem = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)


    def __str__(self):
            return self.nome

class Solicitacao(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE, related_name='solicitacoes')
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    atendida = models.BooleanField(default=False)

    def __str__(self):
          return self.titulo

class Manutencao(models.Model):
    
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='manutencoes')
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    atendida = models.BooleanField(default=False)
    gasto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
          return self.titulo

class Gasto(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='gastos')
    setor = models.CharField(max_length=20)  #Posterioremente será um select
    titulo = models.CharField(max_length=300)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
          return self.titulo

class Viagem(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.PROTECT, related_name='viagens')
    rota = models.ForeignKey(Rota, on_delete=models.PROTECT, related_name='viagens')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT, related_name='viagens')

    data_saida = models.DateTimeField(null = True, blank=True)
    data_chegada = models.DateTimeField(null = True, blank=True)

    def __str__(self):
        return f"{self.motorista.nome} - {self.rota.nome}"