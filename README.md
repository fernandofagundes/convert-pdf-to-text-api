# README #

Formar um wizard de forma dinâmica, onde o usuário poderá passo-a-passo ir complementado as 
informações afim de obter um fluxo de compra de mídia de forma simples.


### Tecnologias envolvidas ###

* [Java 13](https://www.oracle.com/java/technologies/javase-jdk13-downloads.html)
* [MyQSL](https://www.mysql.com/)
* [Bitbucket](https://bitbucket.org/adsimco/jorney/src/master/)

### Antes de Executar pela primeira vez

No MySQL deverá ser criado a base de dados conforme o script resources/db/migration/create_database.sql

* A atualização do banco de dados deverá ser versionada no flyway conforme padrão em 
``` 
resource: db.migration
```
mvn versions:set

### Problemas comuns

```
How to configure "Shorten command line" method for whole project in IntelliJ
```

Add: Inside your .idea folder, change workspace.xml file
```
<property name="dynamic.classpath" value="true" />+
```

To:
```
<component name="PropertiesComponent">
....
</component>
```

### Acesso a API de Recomendação se dá através da URL que está registrada no banco na tabela configuration

```
https://api.adsim.co/recommendation/api/v1
https://api.adsim.co/recommendation/api/v2
```

### Swagger

##### Local
[http://localhost:8585/journey/api/v1/swagger-ui.html](http://localhost:8585/journey/api/v1/swagger-ui.html)

##### QAS
[https://qas.adsim.co/journey/api/v1/swagger-ui.html#](https://qas.adsim.co/journey/api/v1/swagger-ui.html#)


##### Produção
(https://api.adsim.co/journey/api/v1/swagger-ui.html#)[https://api.adsim.co/journey/api/v1/swagger-ui.html#]


##### Homologação
[https://hml.adsim.co/journey/api/v1/swagger-ui.html#](https://hml.adsim.co/journey/api/v1/swagger-ui.html#)