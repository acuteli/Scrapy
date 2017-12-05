from Mydb import Mydb
import requests
import threading
import queue

class ProxyMange(threading.Thread):
    def __init__(self,mydb,proxy_q,lock):
        super(ProxyMange,self).__init__()
        self.mydb = mydb
        self.base_url = 'http://www.baidu.com'
        self.proxy_q = proxy_q
        self.lock = lock

    def drop_ip(self,host):
        print('删除代理:%s' % host)
        sql = 'delete from proxy66 where host="%s"' % host
        self.mydb.exe(sql)

    def run(self):
        while self.proxy_q.qsize() > 0:
            item = self.proxy_q.get()
            proxy = {
                'http': '%s://%s:%s' % (item[2], item[0], item[1]),
                # 'https': '%s://%s:%s' % (item[2], item[0], item[1])

            }
            try:
                response = requests.get(self.base_url,timeout=3,proxies=proxy)
                print(response.status_code)
            except Exception as e:
                self.lock.acquire()
                self.drop_ip(item[0])
                self.lock.release()
            else:
                if not(200 <= response.status_code <=300 ):
                    self.lock.acquire()
                    self.drop_ip(item[0])
                    self.lock.release()

#获取代理队列
def get_proxy():
    proxy_q = queue.Queue()
    sql = 'select * from proxy66'
    res = mydb.query(sql)
    for item in res:
        proxy_q.put(item)
    return proxy_q
if __name__ == '__main__':
    mydb = Mydb('127.0.0.1','root','12345qwert','aynu',charset='utf8')
    lock = threading.Lock()

    proxy_q = get_proxy()
    pm_list = []
    for i in range(150):
        pm = ProxyMange(mydb,proxy_q,lock)
        pm.start()
        pm_list.append(pm)
    for pm in pm_list:
        pm.join()


