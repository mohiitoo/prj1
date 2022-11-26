### prj1
Tis project copy of python schdule package
  For more information, refer to https://schedule.readthedocs.io/en/stable/
####Example
```python
import main
#first job
def Show_name(name):
    print(f"helloow->>> {name}")

#second job
def Nmidonam():
    print('OMG')

#You can assign your job to the following method and get your job done at any time you want.
#any(seconds , minutes , hover , day and week)
main.every().second.do(Show_name, name = "ali" )
main.every(3).seconds.do(Nmidonam)

while True:
    main.run_pending()

```
