# Generated from ConvexPolygon.g4 by ANTLR 4.9
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .ConvexPolygonParser import ConvexPolygonParser
else:
    from ConvexPolygonParser import ConvexPolygonParser


# This class defines a complete generic visitor for a parse tree produced by ConvexPolygonParser.

class ConvexPolygonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ConvexPolygonParser#root.
    def visitRoot(self, ctx: ConvexPolygonParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#vertex.
    def visitVertex(self, ctx: ConvexPolygonParser.VertexContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#convexpolygon.
    def visitConvexpolygon(self, ctx: ConvexPolygonParser.ConvexpolygonContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#asignment.
    def visitAsignment(self, ctx: ConvexPolygonParser.AsignmentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#color.
    def visitColor(self, ctx: ConvexPolygonParser.ColorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#rgb.
    def visitRgb(self, ctx: ConvexPolygonParser.RgbContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#myprint.
    def visitMyprint(self, ctx: ConvexPolygonParser.MyprintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#area.
    def visitArea(self, ctx: ConvexPolygonParser.AreaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#perimeter.
    def visitPerimeter(self, ctx: ConvexPolygonParser.PerimeterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#vertices.
    def visitVertices(self, ctx: ConvexPolygonParser.VerticesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#centroid.
    def visitCentroid(self, ctx: ConvexPolygonParser.CentroidContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#inside.
    def visitInside(self, ctx: ConvexPolygonParser.InsideContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#equal.
    def visitEqual(self, ctx: ConvexPolygonParser.EqualContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#draw.
    def visitDraw(self, ctx: ConvexPolygonParser.DrawContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ConvexPolygonParser#operator.
    def visitOperator(self, ctx: ConvexPolygonParser.OperatorContext):
        return self.visitChildren(ctx)


del ConvexPolygonParser
