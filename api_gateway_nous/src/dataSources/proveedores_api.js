const { RESTDataSource } = require('apollo-datasource-rest'); //Para consumir api. Lo trae Apollo por defecto
const serverConfig = require('../server'); //Tiene las uri de los ms desplegados


class ProveedorAPI extends RESTDataSource { //Una subclase que hereda comportamientos de una superclase llamada RESTdatasource
    constructor() {
        super() //para heredad los atributos de la clase padre RESTDataSource
        this.baseURL = serverConfig.proveedores_api_url //conecta con la url para consumirse

    }
    //Async methods :
    async createProvider(provider) {
        provider = new Object(JSON.parse(JSON.stringify(provider))) //recibe el json provider y lo convierte en un objeto de Javascript. NO ES BUENA PRÁCTICA ESTA FORMA
        return await this.post('/proveedores/', provider) //El this alude al objeto enviado como parámetro del método
        //Como es petición, consume asíncrono que hereda funciones de RESTDataSource (.post)
    }
    async getProviderByName(providerName) {
        let providerId = providerName.idRegister
        return await this.get(`/proveedor/${providerId}`) 
    }
    async updateProvider(providerName) {
        //Otra forma de crear objeto en JS
        providerName = new Object(JSON.parse(JSON.stringify(providerName))) 
        let providerId = providerName.idRegister
        return await this.put(`/proveedor/${providerId}`, providerName)  
    }

    async deleteProvider(providerName) {
        let providerId = providerName.idRegister
        return await this.delete(`/proveedor/${providerId}`)  
    }
    async getAllProvider() {
        return await this.get(`/proveedores/`)
    }

}

module.exports = ProveedorAPI
