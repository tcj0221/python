import time
import stomp
queue_name = 'ItQueue'
topic_name = 'ItTopic'
listener_name = 'ItListener'

try:
    def send_to_queue(msg):
        conn = stomp.Connection10([('114.55.72.246', 61616)])
        conn.start()
        conn.connect()
        conn.send(queue_name, msg)
        conn.disconnect()
    send_to_queue("it_queue")


    # 推送到主题
    def send_to_topic(msg):
        conn = stomp.Connection10([('114.55.72.246', 61616)])
        conn.start()
        conn.connect()
        conn.send(topic_name, msg)
        conn.disconnect()
    send_to_topic("it_topic")


    ##从队列接收消息
    def receive_from_queue():
        conn = stomp.Connection10([('114.55.72.246', 61616)])
        conn.set_listener(listener_name)
        conn.start()
        conn.connect()
        conn.subscribe(queue_name)
        time.sleep(1)  # secs
        conn.disconnect()
    receive_from_queue()


    ##从主题接收消息
    def receive_from_topic():
        conn = stomp.Connection10([('114.55.72.246', 61616)])
        conn.set_listener(listener_name)
        conn.start()
        conn.connect()
        conn.subscribe(topic_name)
        while 1:
            send_to_topic('topic')
            time.sleep(3)  # secs
    receive_from_topic()

except Exception as e:
 #   f_active_log = open("active.log","a+",encoding='utf-8')
 #   f_active_log.writelines(repr(e)+"\n")
 #   f_active_log.close()
     print(e)

