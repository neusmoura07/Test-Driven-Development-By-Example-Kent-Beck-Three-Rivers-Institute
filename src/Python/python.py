class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            exec("self." + self.name + "()")
        except:
            result.testFailed()
        self.tearDown()
        return result

    def tearDown(self):
        pass




class WasRun(TestCase):
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp "

    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self,name)

        
    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception("Este método falha")



class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testFailed(self):
        self.errorCount = self.errorCount + 1

    def testStarted(self):
        self.runCount = self.runCount + 1
    

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)



class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod") 


    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)


    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == results.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run().summary()
TestCaseTest("testFailedResultFormatting").run().summary()
TestCaseTest("testFailedResult").run().summary()

