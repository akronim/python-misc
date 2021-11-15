### checks 
```
python --version
```
```
whereis python
```
```
ls -la /usr/bin/python3
```
```
which python
```
```
ls /usr/lib | grep python
```
```
ls /usr/bin/python*
```
```
apt list --installed | grep python
```
```
update-alternatives --query python
```
```
sudo update-alternatives --list python
```
```
update-alternatives --display python3
```


### set python3 as deafult python
```
update-alternatives --install /usr/bin/python python /usr/bin/python3 1
```


### upgrade from 3.6.9 to 3.9.0
```
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ apt list | grep python3.9
$ sudo apt install python3.9
```

https://linuxhint.com/update_alternatives_ubuntu/
### add alternative python (3.9)
```
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2
$ sudo update-alternatives --config python3
```

#### remove alternative python
```
sudo update-alternatives --remove python3 /usr/bin/python3.9
```

#### restore the old (defulat) symlink of python3
```
sudo rm -rf /usr/bin/python3 && sudo ln -s /usr/bin/python3.6 /usr/bin/python3
```


### remove python 2 - simulate
```
apt remove python --simulate
```
```
sudo apt remove python2.7.* --simulate
```



### remove python
```
sudo apt purge -y python2.7-minimal
```

### You already have Python3 but don't care about the version 
sudo ln -s /usr/bin/python3 /usr/bin/python
sudo apt install python-is-python3

### Same for pip
sudo apt install -y python3-pip
sudo ln -s /usr/bin/pip3 /usr/bin/pip



### always 
python -m pip install <>
















