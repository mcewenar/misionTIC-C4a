package com.misiontic.facturacion_ms.models;
//import org.springframework.data.annotation.Id;
public class Product {
   // @Id
  //  private String idproduct;
    private String name;
    private Integer amount;
    private Integer value;

    public Product( String name, Integer amount, Integer value){
       // this.idproduct = idproduct;
        this.name = name;
        this.amount = amount;
        this.value = value;
    }

    //public String getIdproduct() {
     //   return idproduct;
   // }

   // public void setIdproduct(String idproduct) {
    //    this.idproduct = idproduct;
   // }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getValue() {
        return value;
    }

    public void setValue(Integer value) {
        this.value = value;
    }

    public Integer getAmount() {
        return amount;
    }

    public void setAmount(Integer amount) {
        this.amount = amount;
    }
}
