import API as api
import time
import multiprocessing as mp

def main() -> None:
    # Setting up the API connection
    parentConnectionAPI, childConnectionAPI = mp.Pipe()

    apiProcess = mp.Process(target=api.start, args=(childConnectionAPI,))
    apiProcess.start()

    parentConnectionAPI.send("Hello World from the model")
    time.sleep(5)
    parentConnectionAPI.send({'func': 'loadGui'})
    time.sleep(5)
    try:
        parentConnectionAPI.send({'func': 'transferData', 'args': [3]})
    except ProcessLookupError as e:
        print(e)
        apiProcess.terminate()
        apiProcess.join()
    
    while True:
        if parentConnectionAPI.poll():
            request = parentConnectionAPI.recv()
            print(request)
            break
        
        time.sleep(5)
    
        if apiProcess.is_alive() == False:
            apiProcess.terminate()
            apiProcess.join()
            break

    # while True:
    #     if parentConnectionAPI.poll():
    #         request = parentConnectionAPI.recv()
    #         print(request)
    #         break
        
    #     time.sleep(1)




if __name__ == "__main__":
    main()


    