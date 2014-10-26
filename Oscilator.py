#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, pygame

class Point:
    """ Класс точки """
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
        
    def __eq__(self, right):
        return self._x == right._x and self._y == right._y
    
    def __ne__(self, right):
        return self._x != right._x or self._y != right._y
        
    def __add__(self, right):
        if not isinstance(right, (Point,int,float)): 
            raise TypeError("invalid type")
        if isinstance(right, (int, float)): 
            return Point(self._x + right, self._y + right)
        else: 
            return Point(self._x + right._x, self._y + right._y)

    def __sub__(self, right):
        if not isinstance(right, (Point,int,float)):
            raise TypeError("invalid type")
        if isinstance(right, (int, float)):
            return Point(self._x - right, self._y - right)
        else:
            return Point(self._x - right.x, self._y - right.y)

    def __mul__(self, right):
        if not isinstance(right, (Point,int, float)):
            raise TypeError("invalid type")
        if isinstance(right, (int, float)):
            return Point(self._x * right, self._y * right)
        else:
            return Point(self._x * right.x, self._y * right.y)

    def __div__(self, right):
        if not isinstance(right, (Point,int, float)):
            raise TypeError("invalid type")
        if isinstance(right, (int, float)):
            if right == 0: raise ArithmeticError("right is zero")
            return Point(self._x / right, self._y / right)
        else:
            if right.x == 0 or right.y == 0: raise ArithmeticError("right is zero")
            return Point(self._x / right.x, self._y / right.y)
        
    def normalize(self, right):
        L = self.lenght(right)
        return Point((right._x - self._x) / L, (right._y - self._y) / L)

    def len(self):
        return math.sqrt(self._y ** 2 + self._x ** 2)
    
    def lenght(self, right):
        return math.sqrt((self._y - right._y) ** 2 + (self._x - right._x) ** 2)
    
    def toTuple(self):
        return (int(self._x), int(self._y))
    
    def __repr__(self):
        return "Point[%s x %s]" % (self._x, self._y)
    
    def __str__(self):
        return "Point[%s x %s]" % (self._x, self._y)

class Node:
    """ Класс узла сетки """
    def __init__(self, pos, mass, C, fixed=False):
        self._pos    = pos
        self._vel    = Point()
        self._nodes  = []
        self._lenths = []
        self._fixed  = fixed
        self._mass   = mass
        self._C      = C
        
    def __eq__(self, r):
        return self._pos == r._pos
    
    def __ne__(self, r):
        return self._pos != r._pos

    def update(self, dt):
        if self._fixed:
            return 0.0
        else:
            ef = Point()
            for node, L in zip(self._nodes, self._lenths):
                ef += self.getElasticForce(node, L)
            ff = self.getFrictionalForce()
            gf = self.getGravitationForce()
            
            self._vel += (ef + ff + gf / self._mass) * dt
            self._pos += self._vel * dt
            
            return self._pos.len()
    
    def addNode(self, node):
        self._nodes.append(node)
        self._lenths.append(self.length(node))

    def __repr__(self):
        return "Node[%s: %s, %s]" % (self._pos, len(self._nodes), self._fixed)
    def __str__(self):
        return "Node[%s: %s, %s]" % (self._pos, len(self._nodes), self._fixed)
    
    def length(self, node):
        return math.sqrt( (node._pos._y - self._pos._y) ** 2 + (node._pos._x - self._pos._x)** 2 )
    
    def getElasticForce(self, node, node_distance):
        L = self._pos.lenght(node._pos)
        Lf = 0  if L < node_distance else L - node_distance
        
        direction = self._pos.normalize(node._pos)
        
        return Point(direction._x * self._C * Lf, direction._y * self._C * Lf)
    
    def getFrictionalForce(self):
        return Point(-0.1 * self._vel._x, -0.1 * self._vel._y)
    
    def getGravitationForce(self):
        return Point(0.0, 9.8)

nodesGrid = [
        '211111111111111111112',
        '100001000001000000001',
        '100001000001000000001',
        '100001111111000000001',
        '100000010100000000001',
        '100000011100000000001',
        '100000000000000000001',
        '100000000000000000001',
        '111111111121111111111',
        ]


def main():
    WIDTH                = 640
    HEIGHT               = 480
    NODE_COLOR           = (0, 0, 0)
    FIX_NODE_COLOR       = (255, 0, 0)
    BG_COLOR             = (150, 200, 255)
                         
    NODE_X0              = 10
    NODE_Y0              = 10
                         
    NODE_X_STEP          = 20
    NODE_Y_STEP          = 20
                         
    NODE_MASS            = 10.0
    
    NODE_CONNECT_RADIUS  = 21
    
    NODE_C               = 1
    
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Node grid test")
    
    surface = pygame.Surface((WIDTH, HEIGHT))
    surface.fill(pygame.Color(150, 200, 255))
    
    x = NODE_X0
    y = NODE_Y0
    nodes = []
    connectRadius = NODE_CONNECT_RADIUS

    for nodeLevel in nodesGrid:
        x = NODE_X0
        for node in nodeLevel:
            if node != '0':
                nodes.append(Node(Point(x, y), NODE_MASS, NODE_C, node == '2'))
            x += NODE_X_STEP
        y += NODE_Y_STEP
        
    for node in nodes:
        for nodeInt in nodes:
            if node.length(nodeInt) < connectRadius and node != nodeInt:
                node.addNode(nodeInt)
                
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                raise SystemExit
            
        for node in nodes:
            node.update(1.0 / 30.0)
        
        surface.fill(BG_COLOR)
        for node in nodes:
            for intNode in node._nodes:
                pygame.draw.line(surface, (0, 255, 255), node._pos.toTuple(), intNode._pos.toTuple())
            pygame.draw.circle(surface, FIX_NODE_COLOR if node._fixed else NODE_COLOR , node._pos.toTuple(), 2)
            
        window.blit(surface, (0, 0))
        pygame.display.update()

if __name__ == '__main__':
    main()
