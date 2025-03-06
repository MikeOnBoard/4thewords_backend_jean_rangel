-- create_database.sql
CREATE DATABASE IF NOT EXISTS 4thewords_prueba_jean_rangel;

USE 4thewords_prueba_jean_rangel;

CREATE TABLE IF NOT EXISTS legends (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(100) NOT NULL,
    province VARCHAR(100) NOT NULL,
    canton VARCHAR(100) NOT NULL,
    district VARCHAR(100) NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Datos de ejemplo
INSERT INTO legends (title, description, category, province, canton, district, image_url, created_at) VALUES
('La Llorona', 'Cuenta la leyenda que una mujer que perdió a sus hijos ahogados en un río, vaga por las noches llorando y buscándolos. Su lamento puede escucharse cerca de los ríos y es señal de mal augurio.', 'Fantasmas', 'San José', 'San José', 'Carmen', '/uploads/llorona.jpg', NOW() - INTERVAL FLOOR(RAND() * 30) DAY),
('El Cadejos', 'Un perro negro de ojos rojos y brillantes que aparece en la noche para proteger a los borrachos y personas que caminan solas por la calle. Se dice que es un guardián que evita que las personas caigan en peligros.', 'Criaturas míticas', 'Alajuela', 'Alajuela', 'Alajuela', '/uploads/cadejos.jpg', NOW() - INTERVAL FLOOR(RAND() * 30) DAY),
('La Segua', 'Una hermosa mujer que seduce a los hombres infieles en los caminos solitarios. Cuando el hombre la sube a su caballo, ella se transforma mostrando un rostro de calavera con ojos rojos brillantes.', 'Fantasmas', 'Cartago', 'Cartago', 'Oriental', '/uploads/segua.jpg', NOW() - INTERVAL FLOOR(RAND() * 30) DAY),
('El Padre sin Cabeza', 'Un sacerdote que fue decapitado y ahora vaga por las calles de Cartago durante la noche, asustando a quienes se encuentran con él.', 'Fantasmas', 'Cartago', 'Cartago', 'Occidental', '/uploads/padre.jpg', NOW() - INTERVAL FLOOR(RAND() * 30) DAY),
('La Carreta sin Bueyes', 'Una carreta que recorre las calles durante la noche sin ser jalada por bueyes. El sonido de sus ruedas anuncia la muerte de alguien en el pueblo.', 'Presagios', 'Heredia', 'Heredia', 'Heredia', '/uploads/carreta.jpg', NOW() - INTERVAL FLOOR(RAND() * 30) DAY),
('La Tulevieja', 'Una mujer que abandonó a su hijo recién nacido cerca de un río y fue condenada a buscarlo eternamente. Se la representa con los pechos caídos y llenos de leche, llorando por su hijo perdido.', 'Fantasmas', 'Guanacaste', 'Nicoya', 'Nicoya', '/uploads/tulevieja.jpg', NOW() - INTERVAL FLOOR(RAND() * 30) DAY),
('El Pisuicas', 'Conocido como el diablo costarricense, se aparece en fiestas y bailes para tentar a las personas. Suele vestir elegantemente pero se le reconoce por sus patas de cabra que intenta ocultar.', 'Criaturas míticas', 'San José', 'Escazú', 'Escazú', '/uploads/pisuicas.jpg', NOW() - INTERVAL FLOOR(RAND() * 30) DAY),
('La Mona', 'Una mujer que se transforma en mona y ataca a los hombres infieles. Se dice que es una bruja que utiliza sus poderes para castigar a quienes engañan a sus parejas.', 'Criaturas míticas', 'Puntarenas', 'Puntarenas', 'Puntarenas', '/uploads/mona.jpg', NOW() - INTERVAL FLOOR(RAND() * 30) DAY),
('El Duende', 'Pequeñas criaturas que habitan en los bosques y montañas. Se dice que raptan a los niños y niñas de cabello rubio para convertirlos en uno de ellos.', 'Criaturas míticas', 'Limón', 'Talamanca', 'Bratsi', '/uploads/duende.jpg', NOW() - INTERVAL FLOOR(RAND() * 30) DAY),
('La Bruja Zárate', 'Una poderosa bruja que vivía en Escazú y podía transformarse en diferentes animales. Se cuenta que volaba en forma de bola de fuego por las noches.', 'Brujas', 'San José', 'Escazú', 'Escazú', '/uploads/bruja.jpg', NOW() - INTERVAL FLOOR(RAND() * 30) DAY);
