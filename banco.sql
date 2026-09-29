-- banco.sql
-- Script de criação do banco de dados "barbearia" e da tabela "agendamentos",
-- utilizado pelo sistema de agendamentos da Barbearia Navalha de Ouro.

CREATE DATABASE IF NOT EXISTS barbearia;
USE barbearia;

CREATE TABLE IF NOT EXISTS agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    servico VARCHAR(100),
    preco DECIMAL(10,2),
    barbeiro VARCHAR(50),
    data DATE NOT NULL,
    horario VARCHAR(5),
    status VARCHAR(20) DEFAULT 'Agendado'
);

-- Inserção de agendamentos de exemplo, com datas, barbeiros e status variados
-- (pelo menos 2 "Concluído" e 1 "Cancelado", conforme solicitado)
INSERT INTO agendamentos (cliente, telefone, servico, preco, barbeiro, data, horario, status) VALUES
('João Silva',    '(47) 99999-1111', 'Corte de Cabelo',  35.00, 'Carlos', '2026-09-15', '09:00', 'Agendado'),
('Pedro Souza',   '(47) 99999-2222', 'Barba',            25.00, 'André',  '2026-09-15', '10:00', 'Concluído'),
('Rafael Lima',   '(47) 99999-3333', 'Corte + Barba',    55.00, 'Marcos', '2026-09-15', '11:00', 'Agendado'),
('Lucas Costa',   '(47) 99999-4444', 'Corte de Cabelo',  35.00, 'Carlos', '2026-09-16', '09:30', 'Cancelado'),
('Bruno Alves',   '(47) 99999-5555', 'Sobrancelha',      15.00, 'André',  '2026-09-16', '14:00', 'Concluído'),
('Felipe Rocha',  '(47) 99999-6666', 'Corte + Barba',    55.00, 'Marcos', '2026-09-17', '15:30', 'Agendado'),
('Diego Martins', '(47) 99999-7777', 'Corte de Cabelo',  35.00, 'Carlos', '2026-09-18', '08:00', 'Agendado'),
('Thiago Nunes',  '(47) 99999-8888', 'Barba',            25.00, 'André',  '2026-09-18', '16:00', 'Agendado');
