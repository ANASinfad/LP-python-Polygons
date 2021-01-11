import random
from decimal import Decimal

import polygons

if __name__ is not None and "." in __name__:
    from .ConvexPolygonParser import ConvexPolygonParser
    from .ConvexPolygonVisitor import ConvexPolygonVisitor
else:
    from ConvexPolygonParser import ConvexPolygonParser
    from ConvexPolygonVisitor import ConvexPolygonVisitor


class EvalVisitor(ConvexPolygonVisitor):
    def __init__(self):
        # Mapa para guardar los polígonos.
        self.ListPolygons = {}

    # Visita el árbol de análisis producido por ConvexPolygonParser # root
    def visitRoot(self, ctx: ConvexPolygonParser.RootContext):
        n = next(ctx.getChildren())
        return self.visit(n)

    # Visita el árbol de análisis producido por ConvexPolygonParser # asignment
    def visitAsignment(self, ctx: ConvexPolygonParser.AsignmentContext):
        children = [n for n in ctx.getChildren()]
        polygon = self.visit(children[4])
        # Guardamos el polígono en el mapa.
        self.ListPolygons[children[0].getText()] = polygon
        return polygon

    # Visita el árbol de análisis producido por ConvexPolygonParser # vertex (un punto)
    def visitVertex(self, ctx: ConvexPolygonParser.VertexContext):
        coordinates = [n for n in ctx.getChildren()]
        x = Decimal(coordinates[0].getText())
        y = Decimal(coordinates[2].getText())
        return round(x, 3), round(y, 3)

    # Visita el árbol de análisis producido por ConvexPolygonParser # convexpolygon
    def visitConvexpolygon(self, ctx: ConvexPolygonParser.ConvexpolygonContext):
        vertices = [n for n in ctx.getChildren()]
        points = []
        for element in vertices:
            if element.getText() != '[' and element.getText() != ']' and element.getText() != ' ':
                points.append(self.visit(element))
        poly = polygons.ConvexPolygon()
        poly.contsructWithPoints(points)
        return poly

    # Visita el árbol de análisis producido por ConvexPolygonParser # myprint
    def visitMyprint(self, ctx: ConvexPolygonParser.MyprintContext):
        children = [n for n in ctx.getChildren()]
        result = children[1].getText()
        if result[0] == '"':
            print(result[1:len(result) - 1])
            return result[1:len(result) - 1]
        else:
            return self.visit(children[1]).printPolygon()

    # Visita el árbol de análisis producido por ConvexPolygonParser # area
    def visitArea(self, ctx: ConvexPolygonParser.AreaContext):
        children = [n for n in ctx.getChildren()]
        print(self.visit(children[1]).area())
        return self.visit(children[1]).area()

    # Visita el árbol de análisis producido por ConvexPolygonParser # equal
    def visitEqual(self, ctx: ConvexPolygonParser.EqualContext):
        children = [n for n in ctx.getChildren()]
        left = self.visit(children[1])
        right = self.visit(children[4])
        if left.areEqual(right):
            print("yes")
            return "yes"
        else:
            print("no")
            return "no"

    # Visita el árbol de análisis producido por ConvexPolygonParser # perimeter
    def visitPerimeter(self, ctx: ConvexPolygonParser.PerimeterContext):
        children = [n for n in ctx.getChildren()]
        print(self.visit(children[1]).perimeter())
        return self.visit(children[1]).perimeter()

    # Visita el árbol de análisis producido por ConvexPolygonParser # Vertices (devuelve el numero de vertices de un polígono)
    def visitVertices(self, ctx: ConvexPolygonParser.VerticesContext):
        children = [n for n in ctx.getChildren()]
        print(self.visit(children[1]).numberOfVertices_edges())
        return self.visit(children[1]).numberOfVertices_edges()

    # Visita el árbol de análisis producido por ConvexPolygonParser # centroid
    def visitCentroid(self, ctx: ConvexPolygonParser.CentroidContext):
        children = [n for n in ctx.getChildren()]
        result = self.visit(children[1]).getCentroid()
        print(str(result[0]) + ' ' + str(result[1]))
        return result

    # Visita el árbol de análisis producido por ConvexPolygonParser # inside
    def visitInside(self, ctx: ConvexPolygonParser.InsideContext):
        children = [n for n in ctx.getChildren()]
        left = self.visit(children[1])
        right = self.visit(children[4])
        if right.polygonIsInsidePolygon(left):
            print("yes")
            return "yes"
        else:
            print("no")
            return "no"

    # Visita el árbol de análisis producido por ConvexPolygonParser # color
    def visitColor(self, ctx: ConvexPolygonParser.ColorContext):
        children = [n for n in ctx.getChildren()]
        element = children[1].getText()
        if element in self.ListPolygons.keys():
            rgb = self.visit(children[4])
            polygon = self.ListPolygons[children[1].getText()]
            if rgb[0] > 1.0 or rgb[1] > 1.0 or rgb[2] > 1.0:
                raise Exception("Error: one color of RGB parameter is over 1 ")
            else:
                polygon.assignColor(rgb)
        else:
            raise Exception("Error: variable " + str(element) + " doesn't exists")

    # Visita el árbol de análisis producido por ConvexPolygonParser # rgb
    def visitRgb(self, ctx: ConvexPolygonParser.RgbContext):
        children = [n for n in ctx.getChildren()]
        r = float(children[1].getText())
        g = float(children[3].getText())
        b = float(children[5].getText())
        return [r, g, b]

    # Visita el árbol de análisis producido por ConvexPolygonParser # draw
    def visitDraw(self, ctx: ConvexPolygonParser.DrawContext):
        children = [n for n in ctx.getChildren()]
        polys = []
        outputFile = children[2].getText()
        for i in range(4, len(children)):
            if children[i].getText() != ' ' and children[i].getText() != ',':
                polys.append(self.visit(children[i]))
        polygons.drawPolygons(polys, outputFile)
        return outputFile

    # Visita el árbol de análisis producido por ConvexPolygonParser # operator
    def visitOperator(self, ctx: ConvexPolygonParser.OperatorContext):
        children = [n for n in ctx.getChildren()]
        if ctx.getChildCount() == 1:
            # case polygon
            element = children[0].getText()
            # Devolvemos un polígono
            if element[0] == '[':
                return self.visit(children[0])
            # case ID
            elif element in self.ListPolygons.keys():
                polygon = self.ListPolygons[element]
                return polygon
            else:
                raise Exception("Error: variable " + str(element) + " doesn't exists")
        # Case '!' and '#'
        elif ctx.getChildCount() == 2:
            sign = children[0].getText()
            # Case '#'
            if sign == '#':
                # case polygon
                if children[1].getText()[0] == '[' or children[1].getText()[0] == '(':
                    polygon = self.visit(children[1])
                    points = polygons.getBoundigBox([polygon])
                    poly = polygons.ConvexPolygon()
                    poly.contsructWithPoints(points)
                    return poly
                # case ID
                elif children[1].getText() in self.ListPolygons.keys():
                    polygon = self.ListPolygons[children[1].getText()]
                    points = polygons.getBoundigBox([polygon])
                    poly = polygons.ConvexPolygon()
                    poly.contsructWithPoints(points)
                    return poly
                # case operator
                else:
                    return self.visit(children[1])
            # case '!'
            else:
                num = int(float(children[1].getText()))
                vertices = []
                for i in range(0, num):
                    cordX = round(Decimal(random.random()), 3)
                    cordY = round(Decimal(random.random()), 3)
                    vertices.append((cordX, cordY))
                poly = polygons.ConvexPolygon()
                poly.contsructWithPoints(vertices)
                return poly
        else:
            sign = children[1].getText()
            left = self.visit(children[0])
            right = self.visit(children[2])
            # case intersection
            if sign == ' * ':
                return left.intersectionOfPolygons(right)
            # case union
            elif sign == ' + ':
                return left.unionOfPolygons(right)
            # otherwise
            else:
                return self.visit(children[1])
