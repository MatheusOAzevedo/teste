##import requests

#serial_ativo =raw_input("Digite o numero de serie")

#headers = {
  #  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImE2NTVkMjQwZjQzMTRlNjAyNDBlYTE1ZTI0N2UyNTE5Yjg0MWNmOWI2ZmQwMjViOTI3ZWU5ZTUyMjU5NmUxMjNmM2ZhODA1YTM5ZmEzYThlIn0.eyJhdWQiOiIxIiwianRpIjoiYTY1NWQyNDBmNDMxNGU2MDI0MGVhMTVlMjQ3ZTI1MTliODQxY2Y5YjZmZDAyNWI5MjdlZTllNTIyNTk2ZTEyM2YzZmE4MDVhMzlmYTNhOGUiLCJpYXQiOjE1MzYxNjU5NDksIm5iZiI6MTUzNjE2NTk0OSwiZXhwIjoxNTY3NzAxOTQ5LCJzdWIiOiIxMTc2MSIsInNjb3BlcyI6W119.GAivyPytWcUuRP55DXnZv8jEPPHFW8iEatpK9-N_6haBmJfMpsmmIQteZ_pG1YELSXsKZGFEHa9OOvX9CMQUQ3o-z9jVxp9Oo09mg4BN75t6FJiog8xBHoChrIgxcznQgocPxha3F4iZsqMjq9rTNMHdqn9OwH39OPL5erheaIy2G4AVOI_28D9WSZ4rEFwS3wLtCcZlW8uhnpm44nN20BijWa8CwxMkKaqqFZYRkp6KhE7TAm7jldUZdWNAZZHdclN97K7LZ-MZrKSMG17Vhwf7BJc501nu4UdmBZunhXbHHn7iQ8rnDlsmdflVPhyrxaBFrPTuyGl8E-US16q8HXnD9bGfmmMDZkgMJMJdv5-8r5JQGN41JZegTYFAZnpfSscFOUNQVdR94aG6ivC8m4FTZGWUG8G-yiBrU3XJLMPeA1-2AiC4w_jjemqa5JG8W58PA0Cys5J2zZyF4uhgJAoRwzLsoeOhBZnwd_BfirgGo7dx1Z9aS2-4MwdmkO4o8yW0L2Y8GcgzMt7UB1R9FpS83boQLCzkbihGF0w03gC8XFiZoKK0iwftO6i3bNuUqzBbRFqM1dRtnONkq2PRC1nashtso-r125JLSXWul_aKpzPMmtN8tWcznKN8Yj18fZlfgKQqZ1w4d2ErxzH-Ni-3FVMmkZQiDeJ9bfXlMdA",
 #   "Accept": "application/json"}

#url = 'https://mercadolibre.snipe-it.io/api/v1/hardware/byserial/%s' %serial_ativo
#response = requests.get(url, headers=headers).json()

##print(response)

import requests

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImE2NTVkMjQwZjQzMTRlNjAyNDBlYTE1ZTI0N2UyNTE5Yjg0MWNmOWI2ZmQwMjViOTI3ZWU5ZTUyMjU5NmUxMjNmM2ZhODA1YTM5ZmEzYThlIn0.eyJhdWQiOiIxIiwianRpIjoiYTY1NWQyNDBmNDMxNGU2MDI0MGVhMTVlMjQ3ZTI1MTliODQxY2Y5YjZmZDAyNWI5MjdlZTllNTIyNTk2ZTEyM2YzZmE4MDVhMzlmYTNhOGUiLCJpYXQiOjE1MzYxNjU5NDksIm5iZiI6MTUzNjE2NTk0OSwiZXhwIjoxNTY3NzAxOTQ5LCJzdWIiOiIxMTc2MSIsInNjb3BlcyI6W119.GAivyPytWcUuRP55DXnZv8jEPPHFW8iEatpK9-N_6haBmJfMpsmmIQteZ_pG1YELSXsKZGFEHa9OOvX9CMQUQ3o-z9jVxp9Oo09mg4BN75t6FJiog8xBHoChrIgxcznQgocPxha3F4iZsqMjq9rTNMHdqn9OwH39OPL5erheaIy2G4AVOI_28D9WSZ4rEFwS3wLtCcZlW8uhnpm44nN20BijWa8CwxMkKaqqFZYRkp6KhE7TAm7jldUZdWNAZZHdclN97K7LZ-MZrKSMG17Vhwf7BJc501nu4UdmBZunhXbHHn7iQ8rnDlsmdflVPhyrxaBFrPTuyGl8E-US16q8HXnD9bGfmmMDZkgMJMJdv5-8r5JQGN41JZegTYFAZnpfSscFOUNQVdR94aG6ivC8m4FTZGWUG8G-yiBrU3XJLMPeA1-2AiC4w_jjemqa5JG8W58PA0Cys5J2zZyF4uhgJAoRwzLsoeOhBZnwd_BfirgGo7dx1Z9aS2-4MwdmkO4o8yW0L2Y8GcgzMt7UB1R9FpS83boQLCzkbihGF0w03gC8XFiZoKK0iwftO6i3bNuUqzBbRFqM1dRtnONkq2PRC1nashtso-r125JLSXWul_aKpzPMmtN8tWcznKN8Yj18fZlfgKQqZ1w4d2ErxzH-Ni-3FVMmkZQiDeJ9bfXlMdA",
    "Accept": "application/json"}

opcao_uso =input("Digite 1 para Checkout e 2 para Checkin: ")
serial_ativo = raw_input("Digite o numero do Ativo: ")

if opcao_uso == 1:

#PEGAR ID HARDWARE

    url = 'https://mercadolibre.snipe-it.io/api/v1/hardware/byserial/%s' %serial_ativo
    response = requests.get(url, headers=headers).json()
    hardware_id = response["rows"][0]["id"]
    ativo_name = response["rows"][0]["asset_tag"]
     
    print(ativo_name)
    print("TESTESTETESTETETSTE")





##payload = {'status_id': 22}
#url = "https://mercadolibre.snipe-it.io/api/v1/hardware/%s" % hardware_id
#response = requests.put(url, headers=headers, json=payload)
##print(response.json())