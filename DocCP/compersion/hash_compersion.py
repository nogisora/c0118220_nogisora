import csv
import subprocess
from kubernetes import client, config

config.load_kube_config() #kubernetesのConfigファイルを読み込む
api = client.CustomObjectsApi()
v1 = client.CoreV1Api()
resource = api.list_namespaced_custom_object(group="metrics.k8s.io",version="v1beta1", namespace="default", plural="pods")

for pod in resource["items"]:
    s=pod["metadata"]["name"].replace('n','')
    if 'cpuup-pod1' in s:
        pod_name1=pod["metadata"]["name"]
    elif 'cpuup-pod2' in s:
        pod_name2=pod["metadata"]["name"]
    elif 'cpuup-pod3' in s:
        pod_name3=pod["metadata"]["name"]

subprocess.run('microk8s kubectl cp '+pod_name1+':/app/List1.csv ./List1.csv', shell=True)
subprocess.run('microk8s kubectl cp '+pod_name2+':/app/List2.csv ./List2.csv', shell=True)
subprocess.run('microk8s kubectl cp '+pod_name3+':/app/List3.csv ./List3.csv', shell=True)

with open('List1.csv', 'r') as f1:
    reader1 = csv.reader(f1)
    d1 = dict(map(reversed, reader1))
    k1 = d1.keys()
with open('List2.csv', 'r') as f2:
    reader2 = csv.reader(f2)
    d2 = dict(map(reversed, reader2))
    k2 = d2.keys()
with open('List3.csv', 'r') as f3:
    reader3 = csv.reader(f3)
    d3 = dict(map(reversed, reader3))
    k3 = d3.keys()



result = k1 - k2
result2= k1 - k3


result = map(lambda t: d1[t][2:], result)

result2 = map(lambda t: d1[t][2:], result2)
#for a in result:
    #print(a)

#with open("hashlist.csv", 'w', newline="") as file:
    #spawriter = csv.writer(file)
    #spawriter.writerows(result)





for i in result:
  subprocess.run(f'microk8s kubectl cp {pod_name1}:/app/{i} {i}', shell=True)
  subprocess.run(f'microk8s kubectl cp {i} {pod_name2}:/app/copy/{i}', shell=True)

for i2 in result2:
  subprocess.run(f'microk8s kubectl cp {pod_name1}:/app/{i2} {i2}', shell=True)
  subprocess.run(f'microk8s kubectl cp {i2} {pod_name3}:/app/copy/{i2}', shell=True)
