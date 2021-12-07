package com.misiontic.facturacion_ms.repositories;
import  com.misiontic.facturacion_ms.models.Factura;
import org.springframework.data.mongodb.repository.MongoRepository;
import java.util.List;
public interface FacturaRepository extends MongoRepository<Factura, String> {
    List<Factura> findByUsername (String username);
}

