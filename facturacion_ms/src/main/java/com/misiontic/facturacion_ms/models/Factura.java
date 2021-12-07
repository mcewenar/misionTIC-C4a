package com.misiontic.facturacion_ms.models;
import org.springframework.data.annotation.Id;
import java.util.Date;

import java.util.List;

public class Factura {
    @Id
    private String idfactura;
    private String username;
    private  String address;
    private List<Product> products;
    private Integer totalValue;
    private Date date;

    public Factura(String idfactura, String username, String address, List<Product> products, Integer totalValue, Date date) {
        this.idfactura = idfactura;
        this.username = username;
        this.address = address;
        this.products = products;
        this.totalValue = totalValue;
        this.date = date;

    }

    public String getIdfactura() {
        return idfactura;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void setProducts(List<Product> products) {
        this.products = products;
    }

    public Integer getTotalValue() {
        return totalValue;
    }

    public void setTotalValue(Integer totalValue) {
        this.totalValue = totalValue;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }
}
