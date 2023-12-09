CREATE OR REPLACE FUNCTION valida_comentario_id()
RETURNS TRIGGER AS $$
BEGIN
  IF (
    SELECT COUNT(*)
    FROM sua_tabela
    WHERE pedido_id = NEW.pedido_id AND comentario_id = NEW.comentario_id
  ) > 0 THEN
    RAISE EXCEPTION 'Combinação comentario_id e pedido_id já existe';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER valida_comentario_trigger
BEFORE INSERT
ON olist.star_schema.comentario
FOR EACH ROW
EXECUTE FUNCTION valida_comentario_id()
