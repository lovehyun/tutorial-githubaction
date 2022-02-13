import hello

class TestHello():
  def test_add(self):
    instance = hello.Hello()
    if instance.add(2,3) != 5:
        print('FAILED')
        exit(1)
    print('PASS')

if __name__ == "__main__":
    test = TestHello()
    test.test_add()
