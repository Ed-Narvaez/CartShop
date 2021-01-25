create table producto (
	producto_id SERIAL,
	nombre character varying(150),
	precio float,
	constraint producto_clave primary key(producto_id)
	
)
create table facturas(
	factura_id serial,
	fecha character varying(150),
	subtotal decimal,
	ivg decimal,
	total decimal,
	constraint 	fac_clave primary key(factura_id)
	
)
create table facturas_productos(
	factura_producto_id serial,
	factura_id serial,
	producto_id serial,
	cantidad integer,
	constraint fId foreign key(factura_id) references facturas(factura_id) on delete cascade,
	constraint pId foreign key(producto_id) references productos(producto_id) on delete cascade,
	constraint prim primary key(factura_producto_id)
	
	
)
create table users (
	usuario_id serial,
	nombre character varying(150),
	pass character varying(150),
	constraint pusaurio primary key (usuario_id))
	