# Discription
Simple Item Catalog (Udacity FSND practice)

# Usage
Install Software
- Virtual Box
- Vagrant
- python(2.7)

Clone Virtual Machine config from Udacity repo
```
git clone https://github.com/udacity/fullstack-nanodegree-vm.git fullstack
cd fullstack/vagrant
```

ItemCattalogApp from this repo
```
git clone https://github.com/MasahiroOKUBO/008_MyItemCatalog.git
```

vi client secret
```
vi 008_MyItemCatalog/client_secret_facebook.json
vi 008_MyItemCatalog/client_secret_google.json
```

Start Virtual machine
- !! CAUTION !! vagrant up needs many minutes.
```
vagrant up
vagrant ssh
```

At vagrant shell
```
cd /vagrant/008_MyItemCatalog
python setup1_initializedb.py 
python setup2_lotsofmenus.py
python run_server.py 
```

Browse At MAC
```
open http://localhost:5000/
```

# Close
At vagrant shell
```
CTRL + C

exit

vagrant halt
```



# Thanks to 

- [MDL BLOG](http://materialdesignblog.com/material-design-floating-action-button-for-web-that-really-stands-out/)