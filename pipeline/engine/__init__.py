import sys


def getEngine():

    if 'maya' in sys.executable:
        from pipeline.engine import engine_maya as EngineM
        return EngineM.Maya_Engine()
    elif 'houdini' in sys.executable:
        from pipeline.engine import engine_hou as EngineH
        return EngineH.Houdini_Engine()
    else:
        from pipeline.engine import engine_base as EngineB
        return EngineB.Engine()


#Test
if __name__ == '__main__':
    test = getEngine()
    print(test)
    print(test.implements)
