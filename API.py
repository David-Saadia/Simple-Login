import GUI as gui
import model as MAIN
import multiprocessing as mp
import time

if __name__ == "__main__":
    print("API loaded.")

else:
    print("API imported and loaded.")


def start(parentConnectionModel):
    parentConnectionGUI = None

    while True:
        
        try:
            if parentConnectionModel.poll():
                print("received request")
                request = parentConnectionModel.recv()
                if isinstance(request, dict):
                    match request.get("func"):
                        case "transferData":
                            if parentConnectionGUI is not None:
                                res = transferData(parentConnectionModel, *request["args"], parentConnectionGUI)
                                print("The test was successful" if res else "The test failed")
                            else:
                                print("GUI not loaded.")
                                raise ProcessLookupError("GUI not loaded.")
                            # return
                        case "loadGui":
                            parentConnectionGUI = loadGui()
                            # return
                        case _:
                            print("Unknown request")      
                else:
                    print(request)
            
        except BrokenPipeError as e:
            print(e)
            return

        time.sleep(5)              
                


def loadGui():
     # Setting up the GUI connection
    parentConnectionGUI, childConnectionGUI = mp.Pipe()

    guiProcess = mp.Process(target=gui.start, args=(childConnectionGUI,))
    guiProcess.start()
    return parentConnectionGUI






def transferData(parentConnectionModel, Data, parentConnectionGUI) -> bool:
    parentConnectionGUI.send({'func': 'testImport', 'args': [Data]})

    while True:
        if parentConnectionGUI.poll():
            res = parentConnectionGUI.recv()
            parentConnectionModel.send(res)
            break
        time.sleep(5)
    return True