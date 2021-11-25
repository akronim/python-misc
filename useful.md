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
#### or, better: 
```
sudo ln -s /usr/bin/python3 /usr/bin/python
```
```
sudo apt install python-is-python3
```
#### same for pip
```
sudo apt install -y python3-pip
```
```
sudo ln -s /usr/bin/pip3 /usr/bin/pip
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

#### remove all alternatives
```
sudo update-alternatives --remove-all python
```

#### restore the old (default) symlink of python3
```
sudo rm -rf /usr/bin/python3 && sudo ln -s /usr/bin/python3.9 /usr/bin/python3
```

##### python3.9 > python3 | python3 > python


### remove python 2 - simulate
```
apt remove python --simulate
```
```
sudo apt remove python2.7* --simulate
```
### remove 
#### set aliases
```
sudo apt-get install python-is-python3
```
#### remove
```
sudo apt purge -y python2.7-minimal
```
```
sudo apt-get autoremove --purge
```
#### remove symbolic link
```
sudo ln -s /usr/bin/python2.7 /usr/bin/python
```

#### remove your make altinstall-ed python
```
rm -f /usr/local/bin/python2.7
rm -f /usr/local/bin/pip2.7
rm -f /usr/local/bin/pydoc
rm -rf /usr/local/bin/include/python2.7
rm -f /usr/local/lib/libpython2.7.a
rm -rf /usr/local/lib/python2.7
```
##### You might also have to do
```
rm -f /usr/local/share/man/python2.7.1
rm -rf /usr/local/lib/pkgconfig
rm -f /usr/local/bin/idle
rm -f /usr/local/bin/easy_install-2.7
```

```
prefix='/usr/local/'
pyver='3.6'

rm -rf \
    $HOME/.local/lib/Python${pyver} \
    ${prefix}bin/python${pyver} \
    ${prefix}bin/python${pyver}-config \
    ${prefix}bin/pip${pyver} \
    ${prefix}bin/pydoc \
    ${prefix}bin/include/python${pyver} \
    ${prefix}lib/libpython${pyver}.a \
    ${prefix}lib/python${pyver} \
    ${prefix}bin/python${pyver} \
    ${prefix}bin/pip${pyver} \
    ${prefix}bin/include/python${pyver} \
    ${prefix}lib/libpython${pyver}.a \
    ${prefix}lib/python${pyver} \
    ${prefix}lib/pkgconfig/python-${pyver}.pc \
    ${prefix}lib/libpython${pyver}m.a \
    ${prefix}bin/python${pyver}m \
    ${prefix}bin/2to3-${pyver} \
    ${prefix}bin/python${pyver}m-config \
    ${prefix}bin/idle${pyver} \
    ${prefix}bin/pydoc${pyver} \
    ${prefix}bin/pyvenv-${pyver} \
    ${prefix}share/man/man1/python${pyver}.1 \
    ${prefix}include/python${pyver}m
rm -rI ${prefix}bin/pydoc ## WARN: skip if other pythons in local exist.
```

### always 
python -m pip install <>
















