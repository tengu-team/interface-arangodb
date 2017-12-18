# Interface ArangoDB

 This is a Juju charm interface layer. This interface is used to
 connect to ArangoDB.

#### Requires

```yaml
requires:
  arangodb:
    interface: arangodb
```

```python
@when('arangodb.available')
def connect_to_arangodb(arangodb):
    print(arangodb.host(), arangodb.port(), arangodb.username(), arangodb.password())
)

```

#### Provides

The ArangoDB charm can be found [here](https://jujucharms.com/u/tengu-team/arangodb/):

```yaml
provides:
    db:
      interface: arangodb
```

```python
@when('arangodb.installed', 'db.available')
def configure_interface(db):
    conf = config()
    db.configure(conf['port'], kv.get('username'), kv.get('password'))
```

#### Peers


```yaml
peers:
    cluster:
      interface: arangodb
```

```python
@when('cluster.connected')
def configure_cluster(cluster):
    units = cluster.get_peer_addresses()
    install_cluster(units, True)
```

# Contact Information

 - Sébastien Pattyn <sebastien.pattyn@tengu.io>
 - Dixan Peña Peña <dixan.pena@tengu.io> 
