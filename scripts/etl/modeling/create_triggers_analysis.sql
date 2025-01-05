CREATE TRIGGER trigger_atualiza_custo_m2
BEFORE INSERT OR UPDATE ON imovel
FOR EACH ROW
EXECUTE FUNCTION atualiza_custo_m2();

CREATE TRIGGER trigger_calcular_faixa_area
BEFORE INSERT OR UPDATE ON imovel
FOR EACH ROW
EXECUTE FUNCTION calcular_faixa_area();