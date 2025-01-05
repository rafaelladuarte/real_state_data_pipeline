CREATE OR REPLACE FUNCTION atualiza_custo_m2()
RETURNS TRIGGER AS $$
BEGIN
    NEW.custo_m2 = CASE 
        WHEN NEW.area_m2 > 0 THEN ROUND(NEW.preco::NUMERIC / NEW.area_m2, 2)
        ELSE NULL
    END;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION atualiza_custo_m2()
RETURNS TRIGGER AS $$
BEGIN
    NEW.custo_m2 = CASE 
        WHEN NEW.area_m2 > 0 THEN ROUND(NEW.preco::NUMERIC / NEW.area_m2, 2)
        ELSE NULL
    END;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;