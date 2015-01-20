import zmq
import config


def main():
    context = zmq.Context()

    agent_socket = context.socket(zmq.REP)
    agent_socket.bind("tcp://*:{agent_socket_no}".format(agent_socket_no=config.AGENT_SOCKET_NO))

    processor_socket = context.socket(zmq.PUB)
    processor_socket.bind("tcp://*:{processor_socket_no}".format(processor_socket_no=config.PROCESSOR_SOCKET_NO))

    while True:
        request = agent_socket.recv_multipart()
        print request
        response = {'status': 'ok'}
        agent_socket.send_json(response)
        processor_socket.send_multipart(request)


if __name__ == '__main__':
    main()