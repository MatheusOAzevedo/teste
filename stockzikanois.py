import requests

headers = 

opcao_uso =input("Digite 1 para Checkout e 2 para Checkin: ")
serial_ativo = raw_input("Digite o numero do Ativo: ")

if opcao_uso == 1:

#PEGAR ID HARDWARE

    url = 'https://mercadolibre.snipe-it.io/api/v1/hardware/byserial/%s' %serial_ativo
    response = requests.get(url, headers=headers).json()
    hardware_id = response["rows"][0]["id"]


# PEGAR ID DO USER
    username = raw_input("Digite o usuario: ")
    url = "https://mercadolibre.snipe-it.io/api/v1/users?search=%s" %username
    response = requests.get(url, headers=headers).json()
    user_id = response["rows"][0]["id"]
    tag_ativo = response["rows"][0]["asset_tag"]


# MUDAR STATUS PARA EM USO

    payload = { 'status_id': 22 }
    url = "https://mercadolibre.snipe-it.io/api/v1/hardware/%s" %hardware_id
    response = requests.put(url, headers=headers, json=payload)
    print(response.json())


# FAZER O CHECK-OUT DO EQUIPAMENTO
    payload = { 'assigned_user': user_id, 'checkout_to_type': 'user', 'note': 'Mari TOP e Leo Zika', 'status_label': {"id":22,"name":"En Uso","status_type":"deployable","status_meta":"deployed"} }
    url = "https://mercadolibre.snipe-it.io/api/v1/hardware/%s/checkout" %hardware_id
    response = requests.post(url, headers=headers, json=payload)
    #print(response)

else:

   # PEGAR ID HARDWARE

    url = 'https://mercadolibre.snipe-it.io/api/v1/hardware/byserial/%s' % serial_ativo
    response = requests.get(url, headers=headers).json()
    hardware_id = response["rows"][0]["id"]
    tag_ativo = response["rows"][0]["asset_tag"]

    # MUDAR STATUS PARA EM estoque

    payload = {'status_id': 10}
    url = "https://mercadolibre.snipe-it.io/api/v1/hardware/%s" % hardware_id
    response = requests.put(url, headers=headers, json=payload)
    print(response.json())

    # FAZER O CHECKin DO EQUIPAMENTO
    payload = {'status_label': {"id": 10, "name": "En Stock (Usado)", "status_type": "pending", "status_meta": "pending"}}
    url = "https://mercadolibre.snipe-it.io/api/v1/hardware/%s/checkin" % hardware_id
    response = requests.post(url, headers=headers, json=payload)
    print("Checkin realizado com sucesso!")

    print(response.json())

    #testegit



#DENTRO DO MODULO REQUESTS EXISTEM 4 TIPOS DE FUNCOES - GET = TRAZER INFO, POST - ENVIAR INFO - DELETE - DELETAR INFO - PUT - ATUALIZAR



