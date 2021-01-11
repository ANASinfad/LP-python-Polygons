import math
from decimal import Decimal

from PIL import Image, ImageDraw


class ConvexPolygon:

    # Constructora por defecto.
    def __init__(self):
        self.vertices = []
        self.color = [0, 0, 0]

    # Funcion Para imprimir los vértices del polígono
    def printPolygon(self):
        n = len(self.vertices)
        result = ""
        for i in range(0, n):
            x = self.vertices[i][0]
            y = self.vertices[i][1]
            if i != n - 1:
                result += (str(x) + ' ' + str(y) + ' ')
            else:
                result += (str(x) + ' ' + str(y))
        #print(result)
        return result

    # Método para definir el color del polígono
    def assignColor(self, rgb):
        r = int(rgb[0] * 255)
        g = int(rgb[1] * 255)
        b = int(rgb[2] * 255)
        self.color = [r, g, b]

    # Entrada: Una Lista de vértices. Como precondición la lista de vértices como mínimo debe tener un punto.
    # Salida: Contsruye un Convex hull a partir de una lista de vértices.
    def contsructWithPoints(self, points):
        hull = []
        left = 0
        n = len(points)
        for i in range(1, n):
            if points[i][0] < points[left][0] or (points[i][0] == points[left][0] and points[i][1] < points[left][1]):
                left = i

        p = left
        # Primera iteración para simular el do while.
        hull.append(points[p])
        q = (p + 1) % n
        for j in range(0, n):
            if orientation(points[p], points[q], points[j]) == 2:
                q = j
        p = q
        # Resta de iteraciones
        while p != left:
            hull.append(points[p])
            q = (p + 1) % n
            for j in range(0, n):
                if orientation(points[p], points[q], points[j]) == 2:
                    q = j
            p = q
        self.vertices = hull

    # Método que recibe un vértice como parámetro y comprueba se está dentro del polígono
    def pointIsInsidePolygon(self, point):
        n = len(self.vertices)
        # La lista de vértices tiene que tener como mínimo 3 vértices
        if n < 3:
            return False

        # Creamos un punto extremo. no le ponemos un valor mayor que 10000 para evitar un overflow.(por las multiplicaciones)
        extreme = (10000, point[1])
        count = i = 0

        while True:
            next = (i + 1) % n

            # Comprobamos si el segmento  (point, extreme) se cruza con el segmento (self.vertices[i], self.vertices[next])
            if doIntersect(self.vertices[i], self.vertices[next], point, extreme):

                # Si el point es colineal  con el segmento (self.vertices[i],self.vertices[next]). Se comprueba
                # que point se encuentra en el  segmento (self.vertices[i],self.vertices[next])
                if orientation(self.vertices[i], point, self.vertices[next]) == 0:
                    return onSegment(self.vertices[i], point, self.vertices[next])
                count += 1
            i = next

            if i == 0:
                break
        return count % 2 == 1

    # Método que devuelve el número de vértices del Polígono que también es el número de aristas.
    def numberOfVertices_edges(self):
        return len(self.vertices)

    # Función que comprueba que polygon2 está dentro del polígono self
    # Esta función utiliza el método pointIsInsidePolygon por cada vértice del polygon2
    def polygonIsInsidePolygon(self, polygon2):
        n = len(polygon2.vertices)
        for i in range(0, n):
            if not self.pointIsInsidePolygon(polygon2.vertices[i]):
                return False
        return True

    # El método definido abajo calcula la área de un polígono usando la formula shoelace (Gauss)
    def area(self):
        n = len(self.vertices)
        j = n - 1
        area = Decimal(0.000)

        for i in range(0, n):
            area += (self.vertices[j][0] + self.vertices[i][0]) * (self.vertices[j][1] - self.vertices[i][1])
            j = i
        result = abs(area / Decimal(2.0))
        return round(result, 3)

    # Función que calcula el perímetro de un polígono convexo.
    def perimeter(self):
        perimeter = Decimal(0.0)
        n = len(self.vertices)
        for i in range(0, n):
            j = (i + 1) % n
            perimeter += distance(self.vertices[i], self.vertices[j])

        return round(perimeter, 3)

    # Método que nos permite saber si el Polígono es regular o no.
    def isRegular(self):
        n = len(self.vertices)
        j = n - 1
        d = distance(self.vertices[j], self.vertices[0])
        for i in range(0, n):
            if d != distance(self.vertices[i], self.vertices[j]):
                return False
            j = i
        return True

    # Método que devuelve el Centroide de un Polígono en forma de tupla (coordenadas).
    def getCentroid(self):
        n = len(self.vertices)
        if n == 0:
            return ()
        det = x = y = 0
        for i in range(0, n):
            j = (i + 1) % n
            # Calculamos el determinante
            aux = (self.vertices[i][0] * self.vertices[j][1]) - (self.vertices[j][0] * self.vertices[i][1])
            # Se acumula la suma de los determinantes.
            det += aux
            x += (self.vertices[i][0] + self.vertices[j][0]) * aux
            y += (self.vertices[i][1] + self.vertices[j][1]) * aux

        x /= (3 * det)
        y /= (3 * det)
        centroid = (round(Decimal(x), 3), round(Decimal(y), 3))
        return centroid

    # Método que devuelve la unión de dos polígonos. Que resulta ser un convex hull, y por eso se usa la constructora de la clase.
    def unionOfPolygons(self, polygon2):
        # En points vamos a tener la concatenación de los vértices de self y los vértices de polygon2 sin repeticiones.
        points = list(set(self.vertices) | set(polygon2.vertices))
        union = ConvexPolygon()
        union.contsructWithPoints(points)
        return union

    # Método que devuelve la lista de vértices del polígono
    def getVertices(self):
        return self.vertices

    # Método que devuelve el color de un polígono
    def getColor(self):
        result = '#%02x%02x%02x' % (self.color[0], self.color[1], self.color[2])
        return result

    # Método que devuelve la lista de puntos de intersección entre un polígono y un segmento
    def intersectionofALineAndPolygon(self, A, B):
        result = []
        n = len(self.vertices)
        for i in range(0, n):
            j = (i + 1) % n
            intersectionPoint = intesectionOfTwoLines(self.vertices[i], self.vertices[j], A, B)
            if len(intersectionPoint) != 0:
                result.append(intersectionPoint)
        return result

    # Método que devuelve una lista que contiene los vértices del polígono que es la intersección de los dos polígonos de entrada, si la lista está vacía, eso implica que los polígonos no se cruzan.
    # El método que se utilizó es el que usa el halfplane de cada arista del primer polígono para comprobar la orientación de los vértices que forman las aristas del segundo polígono
    def intersectionOfPolygons(self, polygon2):
        result = []
        n = len(self.vertices)
        m = len(polygon2.vertices)
        if m == 0 or n == 0:
            intersection = ConvexPolygon()
            return intersection
        for i in range(0, n):
            if polygon2.pointIsInsidePolygon(self.vertices[i]):
                addPointWithoutRepetitions(result, self.vertices[i])
        for i in range(0, m):
            if self.pointIsInsidePolygon(polygon2.vertices[i]):
                addPointWithoutRepetitions(result, polygon2.vertices[i])
        for i in range(0, n):
            j = (i + 1) % n
            x = polygon2.intersectionofALineAndPolygon(self.vertices[i], self.vertices[j])
            for element in x:
                addPointWithoutRepetitions(result, element)
        intersection = ConvexPolygon()
        intersection.contsructWithPoints(result)
        return intersection

    # Método que devuelve si dos polígonos son iguales o no.
    def areEqual(self, polygon2):
        return self.vertices == polygon2.vertices

    # Método que define la escala de los vértices de un polígono y devuelve la lista de vértices escalada
    def setScale(self, scaleX, scaleY):
        verticesScaled = []
        for v in self.vertices:
            verticesScaled.append((v[0] * Decimal(scaleX), v[1] * Decimal(scaleY)))
        return verticesScaled


# Método que nos permite añadir puntos a una lista sin repetirlos
def addPointWithoutRepetitions(vertices, point):
    found = False
    for vertex in vertices:
        if vertex == point:
            found = True
            break
    if not found:
        vertices.append(point)


# Función que calcula la distancia entre los puntos p1 y p2
def distance(p1, p2):
    result = math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))
    return Decimal(result)


# Dado tres puntos p1, p2, p3. La función comprueba si p2 se encuentra en el segmento (p1 , p3).
def onSegment(p1, p2, p3):
    if ((p2[0] <= max(p1[0], p3[0])) & (p2[0] >= min(p1[0], p3[0])) & (p2[1] <= max(p1[1], p3[1])) & (
            p2[1] >= min(p1[1], p3[1]))):
        return True
    return False


# Función que nos permite averiguar la orientación que tienen 3 puntos
# Valor 0 => colinear
# Valor 1 => Clockwise
# Valor 2 => Counterclockwise
def orientation(p1, p2, p3):
    value = (((p2[1] - p1[1]) * (p3[0] - p2[0])) - ((p2[0] - p1[0]) * (p3[1] - p2[1])))
    if value == 0:
        return 0  # colinear
    if value > 0:
        return 1  # Clockwise
    else:
        return 2  # Counterclockwise


# Método que comprueba los casos de intersección de los puntos p3 con p1 y p2 / p3 con p1 y p2 / p1 con p3 y p4 / p2 con p3 y p4
def doIntersect(p1, p2, p3, p4):
    orient1 = orientation(p1, p2, p3)
    orient2 = orientation(p1, p2, p4)
    orient3 = orientation(p3, p4, p1)
    orient4 = orientation(p3, p4, p2)

    # Caso general
    if (orient1 != orient2) and (orient3 != orient4):
        return True

    # Casos especiales
    # p1, p2, p3 son colineales y p3 se encuentra en el segmento (p1, p2)
    if (orient1 == 0) and (onSegment(p1, p3, p2)):
        return True

    # p1, p2, p3 son colineales y p4 se encuentra en el segmento (p1, p2)
    if (orient2 == 0) and (onSegment(p1, p4, p2)):
        return True

    # p3, p4, p1 son colineales y p1 se encuentra en el segmento (p3, p4)
    if (orient3 == 0) and (onSegment(p3, p1, p4)):
        return True

    # p3, p4, p2 son colineales y p2 se encuentra en el segmento (p3, p4)
    if (orient4 == 0) and (onSegment(p3, p2, p4)):
        return True
    # otherwise
    return False


# Método que devuelve una lista de vértices que forman el bounding box de polygonsList
def getBoundigBox(polygonsList):
    n = len(polygonsList)
    # La lista finalList tendrá los vértices de todos los polígonos sin repetición
    finalList = []
    # Nos encargamos de eliminar los vértices repetidos en este bucle.
    for i in range(0, n):
        finalList = list(set(polygonsList[i].getVertices()) | set(finalList))
    if len(finalList) == 0:
        return []
    xmax, xmin, ymax, ymin = getMaxAndMinPoints(finalList)
    bottomLeft = (round(Decimal(xmin), 3), round(Decimal(ymin), 3))
    topRight = (round(Decimal(xmax), 3), round(Decimal(ymax), 3))

    topLeft = (bottomLeft[0], topRight[1])
    bottomRight = (topRight[0], bottomLeft[1])
    return [bottomLeft, topRight, topLeft, bottomRight]


# Método que calcula los puntos máximo y mínimo de una lista de vértices
def getMaxAndMinPoints(finalList):
    xmax = finalList[0][0]
    xmin = finalList[0][0]
    ymax = finalList[0][1]
    ymin = finalList[0][1]
    for j in range(1, len(finalList)):
        cordX = finalList[j][0]
        cordY = finalList[j][1]
        if cordX > xmax:
            xmax = cordX
        if cordX < xmin:
            xmin = cordX
        if cordY > ymax:
            ymax = cordY
        if cordY < ymin:
            ymin = cordY
    return xmax, xmin, ymax, ymin


# Método que dibuja los polígonos que hay en la lista polygonsList y lo guarda en el fichero output.png. El bounding box se usa para generar una escala.
def drawPolygons(polygonsList, outputFile):
    img = Image.new('RGB', (400, 400), 'White')
    dib = ImageDraw.Draw(img)
    box = getBoundigBox(polygonsList)
    if len(box) == 0:
        raise NameError('You cannot draw empty polygons')
    elif box[0] == box[1]:
        raise NameError('You cannot draw polygons with 1 vertex')
    topRight = box[1]
    bottomLeft = box[0]
    width = topRight[0] - bottomLeft[0]
    height = topRight[1] - bottomLeft[1]
    if width != 0:
        scaleX = Decimal(398 / width)
    else:
        scaleX = 1
    if height != 0:
        scaleY = Decimal(398 / height)
    else:
        scaleY = 1
    for polygon in polygonsList:
        if polygon.numberOfVertices_edges() > 1:
            color = polygon.getColor()
            dib.polygon(polygon.setScale(scaleX, scaleY), 'White', color)
    img.save(outputFile)


# Este Método recibe como entrada cuatro vértices A, B, C, D y devuelve el punto de intersección en las línea AB y CD,
# si y solo si, el punto de intersección esta incluido en el segmento (AB) y (CD)
# Si la intercección es vacía se devuelve una tupla vacía
def intesectionOfTwoLines(A, B, C, D):
    # Línea AB representada como a1x + b1y = c1
    a1 = B[1] - A[1]
    b1 = A[0] - B[0]
    c1 = a1 * (A[0]) + b1 * (A[1])

    # Línea CD representada como a2x + b2y = c2
    a2 = D[1] - C[1]
    b2 = C[0] - D[0]
    c2 = a2 * (C[0]) + b2 * (C[1])
    # Calculamos el determinante
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return ()
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        onLine1 = onSameLine(x, y, A, B)
        onLine2 = onSameLine(x, y, C, D)
        if onLine1 and onLine2:
            return x, y
        return ()


# Método que comprueba si un punto (x, y) está en el segmento (AB)
def onSameLine(x, y, A, B):
    condition1 = (min(A[0], B[0]) < x or min(A[0], B[0]) == x)
    condition2 = (max(A[0], B[0]) > x or max(A[0], B[0]) == x)
    condition3 = (min(A[1], B[1]) < y or min(A[1], B[1]) == y)
    condition4 = (max(A[1], B[1]) > y or max(A[1], B[1]) == y)
    result = condition1 and condition2 and condition3 and condition4
    return result
