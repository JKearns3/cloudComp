import requests
import json
import time

subscriptionId = "85efd2ee-0fc5-4292-919a-c7e28a24fee9"
bearer = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE3MDAwNTkxMDgsIm5iZiI6MTcwMDA1OTEwOCwiZXhwIjoxNzAwMDY0MjU4LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFZBQUFBMzdqbVUrS29MT1plK0hZRVdSaVZHYjFjMm1uTVJNR1l5eTN6OGhuUmp6dE0xWVJTaVRWTHBIdks0OGlBengzZDYxYnFYTDhiNU1NbCsrZ0p4dDZBM2k0eU5LVi9TQmVhWnRaR0JQdGlVMmM9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiS2Vhcm5zIiwiZ2l2ZW5fbmFtZSI6Ikplbm5pZmVyIiwiZ3JvdXBzIjpbIjgxMDhjNTAzLWQ2NTYtNDJjZi04ZWU0LTg5NDRhZWYwZmFkZSIsIjk3YWY4MTJkLTk2ZTktNGYwMS04YTExLTc1ODAzMzc2MjE3YSIsIjg3ZjYwMDNkLTk0NzAtNDM4Zi1iZmVmLTgxM2IzN2ZjMmI2OCIsIjNlODQ4MDk4LWI0YTEtNDE3ZC1hMWJhLWM5Y2YzZmNlOWY1MSIsIjgzOGEyODlhLTg0YTQtNGNhOC1hZWVjLWIzMWVjMWQ3MWQ0YSIsIjRkYzAzYjlmLTFiNmMtNDQxNS1hYzA1LTgyNDI3MTNjNzUyMCIsIjVhZDdkNmI0LWFkYWYtNGI5ZC05NTdmLTBmM2I2MTRiZWU2MCIsIjhhYzE1NGRkLWQ0NWYtNGM0Ni05NGU1LWJiNzhmZWZhM2FlZiIsIjhjODE4NmVhLTQyYTQtNDRhZi04YTc4LWFlOTE0MDExZTZiNCIsImQyYTZhOGVmLTRkMjYtNGQ5NS1iZDExLWFhMWVjNjE5ZjgxOCJdLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxNDcuMjUyLjE5LjE3NyIsIm5hbWUiOiJDMjEzODMxMjYgSmVubmlmZXIgS2Vhcm5zIiwib2lkIjoiZDA0ZmFkNjktZGUzMS00OTRkLWI0NDMtY2JlNzY0NDQ5OWM2Iiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTQwMjI5ODg0OS0xNzM0NzA1MTMxLTMxMjAwMjQwMDEtNDQ0NTgiLCJwdWlkIjoiMTAwMzIwMDE3REE4QTI1NSIsInJoIjoiMC5BVEVBeXhkamRranBYMDZNN05xOGppX1Yya1pJZjNrQXV0ZFB1a1Bhd2ZqMk1CTXhBRnMuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiMzNwWVBCbVR4bWRQb2NoejZxR3VicUdzU2VDNWVoZGRJWVZ1TFpQRVZmTSIsInRpZCI6Ijc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYSIsInVuaXF1ZV9uYW1lIjoiQzIxMzgzMTI2QG15dHVkdWJsaW4uaWUiLCJ1cG4iOiJDMjEzODMxMjZAbXl0dWR1Ymxpbi5pZSIsInV0aSI6IlY3b2loTGxleDBtSlU1S2pjbXFkQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfY2FlIjoiMSIsInhtc190Y2R0IjoxNTI1MzM4OTQxfQ.ctqnHFd99-dcXX3lMT8L9uk9XZbAJXbpDVvq_gM2idK9xaPXA3d2ofLex2VQjzzJANHl5-20zF1WeIZV54owEYEBVDpWs848R2BwaALsX79VXK2ToTpIt5-JgNJ5V8nYbvKJCFt3-Er4qlI65N115xcBy5OTNWpPVpWzaXz5mUnhFlIsAmX_CthYq6uGpBeu1dh_dDRSTJazni517RMbgpvJ_8SIOQ3KX3W2YFQQ0a1G08MT13Gv7yuurVvfLyefarW0xd-L6r40KrwJCsd8nJuZ5pP2_N5zloUfFTznzVqODllO0yuZIAEvp1b0K3tDB339dwGjDExTME0AThAGFw"

defaultUrl = f"https://management.azure.com/subscriptions/{subscriptionId}/"

resourceGroupName = "lab4py"
virtualNetworkName= "net4py"
subnetName= "snet4py"
ipName = "ip4py"
vmName = "vm4py"
apiVersion = "2021-04-01"

def sendHttpRequest(url, json_data, headers):
    # Sending the POST request with the JSON payload
    response = requests.put(url, data=json_data, headers=headers)

    # Checks for answer
    if response.status_code == 200 or response.status_code == 201:
        print("Successful request")
        response_data = response.json()
        print("Response Data:", response_data)
    else:
        print(f"Error Request. Statuscode: {response.status_code}")

def createResourceGroup():
    global json_data, headers
    # create Resourcegroup
    urlCreateResourceGroup = f"{defaultUrl}resourcegroups/{resourceGroupName}?api-version={apiVersion}"
    # JSON-Data, that you want to send
    createResourceGroupPayloadData = {
        "location": "westeurope"
    }
    # converts Python data to JSON
    json_data = json.dumps(createResourceGroupPayloadData)
    # Set the HTTP headers to set the content type to JSON
    headers = {"Authorization": f"Bearer {bearer}",
               'Content-Type': 'application/json'}
    sendHttpRequest(urlCreateResourceGroup, json_data, headers)

def createVirtualNetwork():
    global json_data
    # create virtual network
    urlCreateVirtualNetwork = f"{defaultUrl}resourcegroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}?api-version=2023-05-01"
    payloadDataCreateVirtualNetwork = {
        "properties": {
            "addressSpace": {
                "addressPrefixes": [
                    "10.0.0.0/16"
                ]
            },
            "flowTimeoutInMinutes": 10
        },
        "location": "westeurope"
    }
    json_data = json.dumps(payloadDataCreateVirtualNetwork)
    sendHttpRequest(urlCreateVirtualNetwork, json_data, headers)

def createSubnet():
    global json_data
    # create subnet
    urlCreateSubnet = f"{defaultUrl}resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}?api-version=2023-05-01"
    payloadDataCreateSubnet = {
        "properties": {
            "addressPrefix": "10.0.0.0/16"
        }
    }
    json_data = json.dumps(payloadDataCreateSubnet)
    sendHttpRequest(urlCreateSubnet, json_data, headers)

def createPublicIpAdress():
    global json_data
    # create public ip adress
    urlCreatePublicIPAdress = f"{defaultUrl}resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{ipName}?api-version=2023-05-01"
    payloadDataCreatePublicIpAdress = {
        "location": "westeurope"
    }
    json_data = json.dumps(payloadDataCreatePublicIpAdress)
    sendHttpRequest(urlCreatePublicIPAdress, json_data, headers)

def createNetworkInterface():
    global networkInterfaceName, json_data
    # create network interface
    networkInterfaceName = "nic4py"
    urlCreateNetworkInterface = f"{defaultUrl}resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{networkInterfaceName}?api-version=2023-05-01"
    payloadDataCreateNetworkInterface = {
        "location": "westeurope",
        "properties": {
            "ipConfigurations": [
                {
                    "name": "ipconfig1",
                    "properties": {
                        "publicIPAddress": {
                            "id": f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{ipName}"
                        },
                        "subnet": {
                            "id": f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}"
                        }
                    }
                }
            ]
        },
       
    }
    json_data = json.dumps(payloadDataCreateNetworkInterface)
    sendHttpRequest(urlCreateNetworkInterface, json_data, headers)

def createVm():
    global json_data
    # create VM
    urlCreateVM = f"{defaultUrl}resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}?api-version=2023-07-01"
    payloadDataCreateVM = {
        "id": f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}",
        "type": "Microsoft.Compute/virtualMachines",
        "location": "westeurope",
        "properties": {
            "osProfile": {
                "adminUsername": "jenni",
                "secrets": [

                ],
                "computerName": f"{vmName}",
                "linuxConfiguration": {
                    "ssh": {
                        "publicKeys": [
                            {
                                "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDcqMQ22QiXP1brEo68rNZBnRizzGMU6/9jmbOCIXzMxnyCROmGC8ptT3h2uzFVScK29weEA8mRBo4DakrQcWU+1q1QH3SUsS8V54lo2u9kZCw/bvp438BO9nnGWwImflEmA/wkK+UlIzMtTTpb1LpNrQseoIOfAAdYFJjMkg6I5KbiZwVqFOsIeE9A2T55wgpiy9garAZVnnssesbtNBEouhQRbpKuldKrBhgoYAcZ3fefn4ZEHZsrNtWiICn96Bq7b65V1YZtI+4BIQIjMfDUr4RJ5ZAGEN/3EQ+Jz3EQkOz3RVhq+sch8nhxAfip2hOpMtC0jCPPnBDABsqylA8zNTAVTPGNoC6txvRHBiWRTuQr+W8Ig9UI6KhgJDrwaBkJRRjGo9sT35a5oURcvcgSWy4ZeW6s1lyhbrclZpc3gUeKqeHtNpCUg/Lh/g6vlEEWnq0ftCxXOYcf1q+UmN11xV4xtvrMgxhjZ61n8ZQDP2c1kVBknc1Qb2kJ6k+qZA0= azureuser@cloudCompVm",      
                                "path": "/home/azureuser/.ssh/authorized_keys",                  
                            }
                        ]
                    },
                    "disablePasswordAuthentication": True
                }
            },
            "networkProfile": {
                "networkInterfaces": [
                    {
                        "id": f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{networkInterfaceName}",
                        "properties": {
                            "primary": True
                        }
                    }
                ]
            },
            "storageProfile": {
                "imageReference": {
                    "sku": "16.04-LTS",
                    "publisher": "Canonical",
                    "version": "latest",
                    "offer": "UbuntuServer"
                },
                "dataDisks": [

                ]
            },
            "hardwareProfile": {
                "vmSize": "Standard_D1_v2"
            },
            "provisioningState": "Creating"
        }
        #"name": f"{vmName}"
    }
    json_data = json.dumps(payloadDataCreateVM)
    sendHttpRequest(urlCreateVM, json_data, headers)

createResourceGroup()
time.sleep(5)
createVirtualNetwork()
time.sleep(5)
createSubnet()
time.sleep(5)
createPublicIpAdress()
time.sleep(20)
createNetworkInterface()
time.sleep(10)
createVm()

