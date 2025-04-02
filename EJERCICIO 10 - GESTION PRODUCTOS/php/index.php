<?php
require_once 'database.php';

header('Content-Type: application/json');

$method = $_SERVER['REQUEST_METHOD'];

switch ($method) {
    case 'POST':
        $data = json_decode(file_get_contents('php://input'), true);

        if (isset($_GET['action'])) {
            $action = $_GET['action'];
            if ($action == 'addProduct') {
                $name = $data['name'];
                $description = $data['description'];
                $price = $data['price'];

                $sql = "INSERT INTO products (name, description, price) VALUES ('$name', '$description', '$price')";

                if ($conn->query($sql) === TRUE) {
                    echo json_encode(['message' => 'Producto creado correctamente']);
                } else {
                    echo json_encode(['error' => $conn->error]);
                }
            }
        }
        break;
    case 'GET':
        if (isset($_GET['id'])) {
            $id = $_GET['id'];

            $sql = "SELECT * FROM products WHERE id = $id";
            $result = $conn->query($sql);

            if ($result->num_rows > 0) {
                $row = $result->fetch_assoc();
                echo json_encode($row);
            } else {
                echo json_encode(['message' => 'Producto no encontrado']);
            }
        }
        break;
    case 'DELETE':
        if (isset($_GET['id'])) {
            $id = $_GET['id'];
            $sql = "DELETE FROM products WHERE id = $id";
            if ($conn->query($sql) === TRUE) {
                echo json_encode(['message' => 'Producto eliminado correctamente']);
            } else {
                echo json_encode(['error' => $conn->error]);
            }
        } else {
            echo json_encode(['error' => 'ID de producto no proporcionado']);
        }
        break;
    default:
        echo json_encode(['error' => 'Metodo no admitido']);
        break;
}

$conn->close();
?>