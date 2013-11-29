#! /usr/bin/ruby


class Tree
    attr_accessor :children, :node_name

    def initialize name, children=[]
    	@children = children
    	@node_name = name
    end

    def visit_all &block
    	visit &block
    	children.each { |c| c.visit_all &block }
    end

    def visit &block
    	block.call self
    end
end

# tree = new Tree('1', new Tree('2', new Tree('3', [])))
# tree = new Tree '1', [new Tree '2', new Tree '3']
tree = Tree.new '1', [Tree.new('2'), Tree.new('3')]
tree.visit_all { |node| puts node.node_name }

