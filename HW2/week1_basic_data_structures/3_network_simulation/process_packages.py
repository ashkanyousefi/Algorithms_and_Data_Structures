# # python3

# from collections import namedtuple

# Request = namedtuple("Request", ["arrived_at", "time_to_process"])
# Response = namedtuple("Response", ["was_dropped", "started_at"])


# class Buffer:
#     def __init__(self, size):
#         self.size = size
#         self.finish_time = []

#     def process(self, request):
#         # write your code here
#         return Response(False, -1)


# def process_requests(requests, buffer):
#     responses = []
#     for request in requests:
#         responses.append(buffer.process(request))
#     return responses


# def main():
#     buffer_size, n_requests = map(int, input().split())
#     requests = []
#     for _ in range(n_requests):
#         arrived_at, time_to_process = map(int, input().split())
#         requests.append(Request(arrived_at, time_to_process))

#     buffer = Buffer(buffer_size)
#     responses = process_requests(requests, buffer)

#     for response in responses:
#         print(response.started_at if not response.was_dropped else -1)


# if __name__ == "__main__":
#     main()


my_list=[(2,3),(3,5),(6,7)]
buffer_size=12

def queue_timer(my_list,buffer_size):
    # from queue import Queue
    import queue
    from time import sleep
    my_queue=queue.Queue()
    for item in my_list:
        if my_queue.empty():
            my_queue.put((item[0],item[1]))
        else:
            print('Overflow Error')
        ready_for_process=my_queue.get()
        sleep(ready_for_process[1])
        status='The system processing for {} the batch number {}'.format(ready_for_process[0],ready_for_process[1]) 
    return status 

print(queue_timer(my_list,buffer_size))

